import os
import json
import pathlib

import pandas as pd

from azure.ai.evaluation import GroundednessEvaluator
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ConnectionType
from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient


from genaiapp import gen_ai_app_query

# load environment variables from the .env file at the root of this repo
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    ASSET_PATH = pathlib.Path(os.getcwd()) / "assets"
    AIPROJECT_CONNECTION_STRING = os.environ.get("AIPROJECT_CONNECTION_STRING")
    EVALUATION_MODEL=os.environ.get("EVALUATION_MODEL")
    AISEARCH_INDEX_NAME = os.environ.get("AISEARCH_INDEX_NAME")

    project = AIProjectClient.from_connection_string(
        AIPROJECT_CONNECTION_STRING,
        credential=DefaultAzureCredential()
    )
    
    connection = project.connections.get_default(
        connection_type=ConnectionType.AZURE_OPEN_AI, 
        include_credentials=True
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

    evaluator_model = {
        "azure_endpoint": connection.endpoint_url,
        "azure_deployment": EVALUATION_MODEL,
        "api_version": "2024-06-01",
        #"api_version": "2024-07-18",
        "api_key": connection.key,
    }

    # Initialzing Groundedness Evaluator
    groundedness_eval = GroundednessEvaluator(evaluator_model)

    # Load evaluation set
    query_and_truth_dataset = []
    with open(ASSET_PATH / "chat_eval_data.jsonl") as fp:
        for row in fp.readlines():
            query_and_truth_dataset.append(json.loads(row))
    
    # For each row, call the gen AI app
    results = []
    for row in query_and_truth_dataset[0:3]:
        query = row["query"]
        print(f'Querying: {query}')
        try:
            resp_and_context = gen_ai_app_query(
                query,
                chat_completion_client=chat,
                embeddings_client=embeddings,
                search_client=az_search_client
            )
        except Exception as ex:
            print(type(ex))
            raise ex
        query_and_resp_and_context = {"query":query, **resp_and_context}
        #query_and_resp_and_context.update({"context":['dummy context']})
        print(query_and_resp_and_context)
        try:
            groundedness_score = groundedness_eval(**query_and_resp_and_context)
        except Exception as ex:
            print(type(ex))
            raise ex
        evaluated_response = {"groundedness": groundedness_score, **query_and_resp_and_context}
        results.append(evaluated_response)

    df = pd.DataFrame.from_records(results)
    df.to_json("./evaluation-results.json")