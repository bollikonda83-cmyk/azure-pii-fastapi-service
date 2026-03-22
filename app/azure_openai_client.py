import os
from openai import AzureOpenAI

def get_azure_openai_client() -> AzureOpenAI:
    print("DEBUG ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
    print("DEBUG KEY:", os.getenv("AZURE_OPENAI_KEY"))
    print("DEBUG DEPLOYMENT:", os.getenv("AZURE_OPENAI_DEPLOYMENT"))

    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-02-01"
    )
