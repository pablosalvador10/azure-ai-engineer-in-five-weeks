import os
import logging
import asyncio
import time
from typing import List, Optional, Tuple

import streamlit as st
from pymongo import MongoClient
from pymongo.collection import Collection
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import urllib.parse

# If you have a local helper to load environment variables
from dotenv import load_dotenv

# Assuming you have a local module for AzureOpenAIManager
from src.aoai.aoai_helper import AzureOpenAIManager

# ----------------------------- #
#         Configuration         #
# ----------------------------- #

# Load environment variables from your .env file
load_dotenv(".env")

# Set up logging so we can see what's happening in the terminal/logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Configure how Streamlit renders the web app
st.set_page_config(
    page_title="AI Engineering in Five Weeks Chatbot 🚀",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Display a main title in the Streamlit app
st.title("🤖 MSAI:495 Assistant")

# ----------------------------- #
#     Initialize Session State  #
# ----------------------------- #

def initialize_session_state() -> None:
    """
    Prepares all the data we want to store in Streamlit's session state,
    such as toggles, cached data, and references to our database and clients.
    """
    # Check if caching is enabled or disabled; default to True if not specified
    if "enable_cache" not in st.session_state:
        st.session_state["enable_cache"] = True
        logger.info("Initialized 'enable_cache' to True.")

    # Keep track of user and assistant messages in a "chat_history"
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        logger.info("Initialized 'chat_history' to an empty list.")

    # Create and store a manager for MongoDB (CosmosDB) if it doesn't exist yet
    if "cosmosdb_manager" not in st.session_state:
        try:
            st.session_state["cosmosdb_manager"] = initialize_cosmosdb_manager()
            logger.info("Connected to CosmosDB (Mongo API).")
        except Exception as e:
            logger.error(f"Failed to connect to CosmosDB: {e}")
            st.error("Failed to connect to the database. Please check your configuration.")
            st.stop()  # Stop if we can't access the database

    # Create and store a manager for Azure OpenAI if it doesn't exist yet
    if "azure_openai_client_4o" not in st.session_state:
        try:
            st.session_state["azure_openai_client_4o"] = AzureOpenAIManager(
                api_key=os.getenv('AZURE_OPENAI_KEY'),
                api_version=os.getenv('AZURE_OPENAI_API_VERSION', "2023-05-15"),
                azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
                embedding_model_name=os.getenv('AZURE_OPENAI_EMBEDDING_DEPLOYMENT'),
                completion_model_name=os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_ID'),
            )
            logger.info("Azure OpenAI Manager initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize Azure OpenAI Manager: {e}")
            st.error("Failed to initialize AI components. Please check your configuration.")
            st.stop()

    # Create and store an Azure Cognitive Search client if it doesn't exist yet
    if "search_client" not in st.session_state:
        try:
            st.session_state["search_client"] = SearchClient(
                endpoint=os.getenv("AZURE_AI_SEARCH_SERVICE_ENDPOINT"),
                index_name=os.getenv("AZURE_SEARCH_INDEX_NAME", "lab-ai-index"),
                credential=AzureKeyCredential(os.getenv("AZURE_AI_SEARCH_ADMIN_KEY")),
            )
            logger.info("Azure Search Client initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize Azure Search Client: {e}")
            st.error("Failed to initialize search components. Please check your configuration.")
            st.stop()

    # Additional default settings that we'll keep in session state
    defaults = {
        "conversation_history": [],
        "ai_response": "",
        "messages": [
            {
                "role": "assistant",
                "content": "Hey, this is your AI assistant. Please type your question to get started!"
            }
        ],
        "uploaded_files": [],
        "disable_chatbot": False,
        "initialized_default": False,
        "similarity_threshold": 0.96,
    }

    # Assign default values if they're not already present in session state
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
            logger.info(f"Initialized '{key}' with default value.")

def initialize_cosmosdb_manager() -> Collection:
    """
    Connect to MongoDB (CosmosDB) using credentials from environment variables,
    and return a reference to a specific Collection in the database.
    """
    COSMOS_MONGO_USER = os.environ.get('COSMOS_MONGO_USER')
    COSMOS_MONGO_PWD = os.environ.get('COSMOS_MONGO_PWD')
    COSMOS_MONGO_SERVER = os.environ.get('COSMOS_MONGO_SERVER')

    DB_NAME = 'ExampleDB'
    COLLECTION_NAME = "ExampleCollection"

    # If any required environment variable is missing, throw an error
    if not all([COSMOS_MONGO_USER, COSMOS_MONGO_PWD, COSMOS_MONGO_SERVER]):
        logger.error("MongoDB environment variables are not fully set.")
        raise ValueError("Missing MongoDB configuration in environment variables.")

    # Build the MongoDB connection string with appropriate URL-encoding of the password
    connection_str = (
        "mongodb+srv://"
        + urllib.parse.quote(COSMOS_MONGO_USER)
        + ":"
        + urllib.parse.quote(COSMOS_MONGO_PWD)
        + "@"
        + COSMOS_MONGO_SERVER
        + "?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
    )

    mongo_client = MongoClient(connection_str)
    db = mongo_client[DB_NAME]

    # Create the collection if it doesn't exist yet
    if COLLECTION_NAME not in db.list_collection_names():
        db.create_collection(COLLECTION_NAME)
        logger.info(f"Created collection '{COLLECTION_NAME}'.")
    else:
        logger.info(f"Using existing collection: '{COLLECTION_NAME}'.")

    return db[COLLECTION_NAME]

# ----------------------------- #
#         Helper Functions      #
# ----------------------------- #

def generate_embeddings(text: str) -> List[float]:
    """
    Generate a vector embedding for the given text using Azure OpenAI embeddings.
    Embeddings are typically used for semantic search or similarity comparisons.
    """
    try:
        embedding_response = st.session_state["azure_openai_client_4o"].generate_embedding(text)
        return embedding_response.data[0].embedding
    except Exception as e:
        logger.error(f"Error generating embedding: {e}")
        return []

def retrieve_documents_from_azure_ai_search(query: str) -> List[dict]:
    """
    Talk to Azure Cognitive Search with the given query,
    and return up to 5 relevant documents (with content + metadata).
    """
    try:
        search_client = st.session_state["search_client"]
        semantic_config = os.getenv("AZURE_SEARCH_SEMANTIC_CONFIG_NAME", None)

        if semantic_config:
            # If we have semantic configuration, perform a semantic search
            results = search_client.search(
                search_text=query,
                top=5,
                query_type="semantic",
                query_caption="extractive",
                query_answer="extractive",
                semantic_configuration_name=semantic_config,
            )
            logger.info("Performed semantic search.")
        else:
            # Otherwise, just do a keyword-based search
            results = search_client.search(search_text=query, top=5)
            logger.info("Performed keyword search.")

        docs = []
        for doc in results:
            chunk_text = doc.get("chunk", "")
            doc_name = doc.get("parent_path", "UnknownSource")

            docs.append({
                "content": chunk_text,
                "metadata": doc_name
            })

        logger.info(f"Retrieved {len(docs)} documents from search.")
        return docs

    except Exception as e:
        logger.error(f"Error retrieving documents: {e}")
        st.error("Failed to retrieve documents. Please try again later.")
        return []

async def generate_llm_response(query: str, context: List[str]) -> str:
    """
    Calls AzureOpenAIManager to produce a chat-based response. 
    We feed the documents' content as "Context" and the user query as "User Query."
    """
    try:
        prompt = f"""
        Context:
        {context}

        User Query:
        {query}

        Instructions:
        - If sufficient context exists, provide an answer.
        - If insufficient information, respond with "I'm sorry, I don't have enough information."
        """

        logger.info("Generating AI response...")
        logger.debug(f"User Prompt: {prompt}")

        # We ask the manager to generate a chat response from the prompt
        # stream=False means we wait for the full response rather than streaming tokens
        response = await st.session_state["azure_openai_client_4o"].generate_chat_response(
            query=prompt,
            system_message_content=(
                "You are a chatbot assistant, tasked with answering user queries "
                "based on the provided context."
            ),
            conversation_history=[],
            stream=False,
            max_tokens=3000,
        )

        logger.info("AI response generated successfully.")
        return response
    except Exception as e:
        logger.error(f"Error generating LLM response: {e}")
        return "I'm sorry, but I encountered an error processing your request."

def store_response(
    query: str,
    response: str,
    context: List[str],
    sources: List[str],
    collection: Collection
) -> None:
    """
    Store the user's query, the assistant's response,
    the embedding of the query, and references to source documents in MongoDB.
    """
    try:
        entry = {
            "query": query,
            "response": response,
            "context": context,
            "queryVector": generate_embeddings(query),
            "sources": sources,
            "created_at": time.time(),
        }
        collection.insert_one(entry)
        logger.info("Stored response in cache.")
    except Exception as e:
        logger.error(f"Error storing response: {e}")

def search_cached_response(
    query: str,
    collection: Collection,
    similarity_threshold: float
) -> Optional[Tuple[Optional[str], Optional[List[str]]]]:
    """
    Look in MongoDB to see if we've answered a similar query before.
    Uses vector similarity to find the closest match, if any,
    and returns (response, sources) if the similarity meets our threshold,
    otherwise (None, None).
    """
    try:
        embedding = generate_embeddings(query)

        pipeline = [
            {
                "$vectorSearch": {
                    "index": "VectorSearchIndex",  # Index name in Mongo or Cosmos DB
                    "path": "queryVector",
                    "queryVector": embedding,
                    "numCandidates": 5,
                    "limit": 5,
                }
            },
            {
                "$project": {
                    "similarityScore": {"$meta": "searchScore"},
                    "response": 1,
                    "sources": 1
                }
            },
        ]
        results = list(collection.aggregate(pipeline))
        if not results:
            logger.info("No cached responses found.")
            return None, None

        # Find the highest-scoring result
        best_result = max(results, key=lambda x: x.get("similarityScore", 0.0))
        if best_result.get("similarityScore", 0.0) >= similarity_threshold:
            logger.info("Found a cached response with sufficient similarity.")
            return best_result.get("response"), best_result.get("sources")
        else:
            logger.info("No cached response met the similarity threshold.")
            return None, None

    except Exception as e:
        logger.error(f"Error during cache search: {e}")
        return None, None

def run_async(coro):
    """
    We need a simple helper function for running async coroutines 
    from a synchronous environment (i.e., inside Streamlit).
    """
    try:
        return asyncio.run(coro)
    except Exception as e:
        logger.error(f"Asyncio run failed: {e}")
        return "I'm sorry, I encountered an error processing your request."

async def chatbot_logic(query: str) -> str:
    """
    This function orchestrates the conversation:
      1. Check if we have a cached answer that's sufficiently similar to the new query.
      2. If so, return that answer along with references.
      3. If not, fetch documents from Azure Search, call the LLM,
         store the new answer in our cache, and display references.
    """
    start_time = time.time()
    collection = st.session_state["cosmosdb_manager"]

    # 1. Attempt to retrieve a cached answer if caching is enabled
    if st.session_state.get("enable_cache", True):
        similarity_threshold = st.session_state.get("similarity_threshold", 0.96)
        cached_response, cached_sources = search_cached_response(query, collection, similarity_threshold)
        if cached_response:
            duration = time.time() - start_time
            references_str = "\n\n**References:**\n"
            seen_sources = set()
            for i, src in enumerate(cached_sources, start=1):
                # Only list each source once
                if src not in seen_sources:
                    seen_sources.add(src)
                    references_str += f"{i}. {src}\n"

            return (
                f"🗄️ **(Cached Response in {duration:.2f}s)**\n\n{cached_response}"
                f"{references_str}"
            )

    # 2. If no suitable cache entry found, ask Azure AI Search for relevant docs
    retrieved_docs = retrieve_documents_from_azure_ai_search(query)
    if not retrieved_docs:
        logger.warning("No documents retrieved from Azure AI Search.")
        return "I'm sorry, I couldn't retrieve any relevant documents to answer your query."

    # Gather the chunk texts to pass as context
    context_texts = [doc["content"] for doc in retrieved_docs]

    # 3. Generate a response from Azure OpenAI
    llm_response = await generate_llm_response(query, context_texts)
    if not llm_response:
        return "I'm sorry, I couldn't generate a response at this time."

    duration = time.time() - start_time

    # 4. We'll store references so that the user can see the doc sources
    all_sources = [doc["metadata"] for doc in retrieved_docs]

    # Save this brand-new response in the cache
    store_response(query, llm_response['response'], context_texts, all_sources, collection)

    # 5. Build a references block to display to the user
    references_str = "\n\n**References:**\n"
    seen_sources = set()
    for i, src in enumerate(all_sources, start=1):
        if src not in seen_sources:
            seen_sources.add(src)
            references_str += f"{i}. {src}\n"

    final_answer = (
        f"⏳ **(LLM Response in {duration:.2f}s)**\n\n{llm_response['response']}"
        f"{references_str}"
    )
    return final_answer

# ----------------------------- #
#          UI Components        #
# ----------------------------- #

def configure_sidebar():
    """
    Builds the sidebar in the Streamlit UI, allowing users
    to toggle caching and clear chat history, among other tasks.
    """
    with st.sidebar:
        st.title("Chat Settings & Tools")

        with st.expander("🔧 Caching Settings", expanded=True):
            # Let users switch caching on or off
            enable_cache = st.checkbox(
                "Enable Response Caching",
                value=st.session_state.get("enable_cache", True)
            )
            st.session_state["enable_cache"] = enable_cache
            st.markdown(
                "_This enables caching via MongoDB to retrieve previous responses quickly._"
            )

            st.divider()

            # Let users set how strictly new queries must match old ones
            similarity_threshold = st.slider(
                "Set Similarity Threshold",
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.get("similarity_threshold", 0.96),
                step=0.01
            )
            st.session_state["similarity_threshold"] = similarity_threshold

        st.divider()

        # A button to clear all chat history from the current session
        if st.button("Clear Chat History"):
            st.session_state["chat_history"] = []
            st.success("Chat history cleared.")

def chat_interface():
    """
    Displays the main chat area, showing user and assistant messages,
    plus a text input for the user to ask new questions.
    """
    if not st.session_state.get("initialized_default"):
        # If this is the first time, show a greeting from the assistant
        st.session_state["chat_history"] = [
            {
                "role": "assistant",
                "content": "🚀 Hello! How can I help you today? I'm here to assist with your questions."
            }
        ]
        st.session_state["initialized_default"] = True

    # Render each message in the chat history
    for message in st.session_state["chat_history"]:
        role = message["role"]
        content = message["content"]
        avatar = "🧑‍💻" if role == "user" else "🤖"
        with st.chat_message(role, avatar=avatar):
            st.markdown(content, unsafe_allow_html=True)

    # Provide a textbox where the user can type their message
    user_query = st.chat_input("Type your message here...")

    if user_query:
        # First, display the user's message
        st.session_state["chat_history"].append({"role": "user", "content": user_query})
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(user_query, unsafe_allow_html=True)

        # Then, let the AI generate a reply asynchronously
        with st.chat_message("assistant", avatar="🤖"):
            response = run_async(chatbot_logic(user_query))
            st.session_state["chat_history"].append({"role": "assistant", "content": response})
            st.markdown(response, unsafe_allow_html=True)

# ----------------------------- #
#            Main App           #
# ----------------------------- #

def main():
    """
    This is the main entry point for our Streamlit app:
      - Initialize session state
      - Configure the sidebar
      - Show a divider
      - Launch the chat interface
    """
    initialize_session_state()
    configure_sidebar()
    st.markdown("---")
    chat_interface()

if __name__ == "__main__":
    main()
