import os
from app.azure_openai_client import get_azure_openai_client
from app.azure_openai_client import get_azure_openai_client
from app.clients.openai_client import get_openai_client

def summarize_text(text: str) -> str:

    print("DEBUG ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
    print("DEBUG KEY:", os.getenv("AZURE_OPENAI_KEY"))
    print("DEBUG DEPLOYMENT:", os.getenv("AZURE_OPENAI_DEPLOYMENT"))

    client = get_azure_openai_client()

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "You are a helpful summarization assistant."},
            {"role": "user", "content": text}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content

