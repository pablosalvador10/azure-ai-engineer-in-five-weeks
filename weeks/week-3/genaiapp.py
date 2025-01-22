"""
# Evaluation Using Prompty

This homework is based off of a Microsoft tutorial. You can see all three parts of the tutorial for developing a RAG pattern solution and evaluating. The sample has been adapted to be ran in a notebook.

**Tutorial**

* https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/copilot-sdk-create-resources?tabs=windows
* https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/copilot-sdk-build-rag
* https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/copilot-sdk-evaluate

**Additional Resources**

* https://learn.microsoft.com/en-us/python/api/overview/azure/ai-evaluation-readme?view=azure-python
* https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/evaluate-sdk
"""

import os
import json
import logging
import pathlib
from pathlib import Path
import sys

from azure.ai.inference import ChatCompletionsClient, EmbeddingsClient
from azure.ai.inference.prompts import PromptTemplate
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from opentelemetry import trace


# load environment variables from the .env file in the current working directory
from dotenv import load_dotenv
load_dotenv()

## Constants
# Assumes you are running this script from the week-3 folder
ASSET_PATH = pathlib.Path(os.getcwd()) / "assets"
AIPROJECT_CONNECTION_STRING = os.environ.get("AIPROJECT_CONNECTION_STRING")
AISEARCH_INDEX_NAME = os.environ.get("AISEARCH_INDEX_NAME")
EVALUATION_MODEL=os.environ.get("EVALUATION_MODEL")
EMBEDDINGS_MODEL=os.environ.get("EMBEDDINGS_MODEL")
INTENT_MAPPING_MODEL=os.environ.get("INTENT_MAPPING_MODEL")
CHAT_MODEL=os.environ.get("CHAT_MODEL")

# Configure an root app logger that prints info level logs to stdout
logger = logging.getLogger("app")
tracer = trace.get_tracer("app")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


# Returns a module-specific logger, inheriting from the root app logger
def get_logger(module_name):
    return logging.getLogger(f"app.{module_name}")

@tracer.start_as_current_span(name="get_documents_with_intent")
def get_documents_with_intent(messages: list, context: dict, chat_completion_client: ChatCompletionsClient, embeddings_client:EmbeddingsClient, search_client:SearchClient) -> dict:
    """
    In the samples from Microsoft this function was named "get_product_documents"
    The purpose of this function is to discover documents that can help ground
    the response to the user's query.
    
    * It does so by first executing a chat completion with a prompt to discover the
    user's intention.
    * Next we need to convert the intent and query into a vector representation.
    * Lastly, we actually query the search index with the search query and the vector representation
    """
    if context is None:
        context = {}

    overrides = context.get("overrides", {})
    top = overrides.get("top", 2)

    # generate a search query from the chat messages
    intent_prompty = PromptTemplate.from_prompty(Path(ASSET_PATH) / "intent_mapping.prompty")

    intent_mapping_response = chat_completion_client.complete(
        model=INTENT_MAPPING_MODEL,
        messages=intent_prompty.create_messages(conversation=messages),
        **intent_prompty.parameters,
    )

    search_query = intent_mapping_response.choices[0].message.content
    logger.debug(f"🧠 Intent mapping: {search_query}")

    # generate a vector representation of the search query
    embedding = embeddings_client.embed(model=EMBEDDINGS_MODEL, input=search_query)
    search_vector = embedding.data[0].embedding

    # search the index for documents matching the search query
    vector_query = VectorizedQuery(vector=search_vector, k_nearest_neighbors=top, fields="contentVector")

    search_results = search_client.search(
        search_text=search_query, vector_queries=[vector_query], select=["id", "content", "filepath", "title", "url"]
    )

    documents = [
        {
            "id": result["id"],
            "content": result["content"],
            "filepath": result["filepath"],
            "title": result["title"],
            "url": result["url"],
        }
        for result in search_results
    ]

    # add results to the provided context
    if "thoughts" not in context:
        context["thoughts"] = []

    # add thoughts and documents to the context object so it can be returned to the caller
    context["thoughts"].append(
        {
            "title": "Generated search query",
            "description": search_query,
        }
    )

    if "grounding_data" not in context:
        context["grounding_data"] = []
    context["grounding_data"].append(documents)

    logger.debug(f"📄 {len(documents)} documents retrieved: {documents}")
    return documents


@tracer.start_as_current_span(name="grounded_response_with_docs_after_intention")
def grounded_response_with_docs_after_intention(messages: list, context: dict, chat_completion_client: ChatCompletionsClient, embeddings_client:EmbeddingsClient, search_client:SearchClient) -> dict:
    """
    In the samples from Microsoft this function was named "grounded_response_with_docs_after_intention"
    The purpose of this function is to respond, in a natural language way, to
    the user's query by first looking for understanding user intent, searching
    for documents relevant to the query and intent, and then grounding the
    response to ensure no misbehavior from the app.
    """
    if context is None:
        context = {}

    documents = get_documents_with_intent(
        messages, 
        context,
        chat_completion_client=chat_completion_client,
        embeddings_client=embeddings_client,
        search_client=search_client
    )

    # do a grounded chat call using the search results
    grounded_chat_prompt = PromptTemplate.from_prompty(Path(ASSET_PATH) / "grounded_chat.prompty")

    system_message = grounded_chat_prompt.create_messages(documents=documents, context=context)
    response = chat_completion_client.complete(
        model=CHAT_MODEL,
        messages=system_message + messages,
        **grounded_chat_prompt.parameters,
    )
    logger.info(f"💬 Response: {response.choices[0].message}")

    # Return a chat protocol compliant response
    return {"message": response.choices[0].message, "context": context}

def gen_ai_app_query(query:str, chat_completion_client: ChatCompletionsClient, embeddings_client:EmbeddingsClient, search_client:SearchClient):
    """
    Execute the query against your RAG application
    """
    response = grounded_response_with_docs_after_intention(
        messages=[{"role": "user", "content": query}],
        context=None,
        chat_completion_client=chat_completion_client,
        embeddings_client=embeddings_client,
        search_client=search_client
    )
    return {"response": response["message"].content, "context": response["context"]["grounding_data"]}

if __name__ == "__main__":
    """
    This is a console application that lets you execute a query from your RAG
    application.
    """
    ## Create Clients
    project = AIProjectClient.from_connection_string(
        AIPROJECT_CONNECTION_STRING,
        credential=DefaultAzureCredential()
    )
    # create a chat completion client to support determining intent from query / chat history
    chat = project.inference.get_chat_completions_client()
    # create a vector embeddings client that will be used to generate vector embeddings
    embeddings = project.inference.get_embeddings_client()

    # use the project client to get the default search connection
    # If this part fails, please be sure to connect your Azure AI Search service
    ## https://learn.microsoft.com/en-us/azure/ai-studio/tutorials/copilot-sdk-create-resources?tabs=windows#connect
    search_connection = project.connections.get_default(
        connection_type=ConnectionType.AZURE_AI_SEARCH, include_credentials=True
    )

    # Create a search index client using the search connection
    # This client will be used to query your documents
    az_search_client = SearchClient(
        index_name=AISEARCH_INDEX_NAME,
        endpoint=search_connection.endpoint_url,
        credential=AzureKeyCredential(key=search_connection.key),
    )
    # Call the Gen AI Application we've developed with a sample query
    response = gen_ai_app_query(
        query = "What is the perks plus benefit?",
        chat_completion_client=chat,
        embeddings_client=embeddings,
        search_client=az_search_client
    )
    print (json.dumps(response, indent=2))