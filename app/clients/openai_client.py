import os
from openai import AzureOpenAI

def get_openai_client() -> AzureOpenAI:
    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-01",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    )
