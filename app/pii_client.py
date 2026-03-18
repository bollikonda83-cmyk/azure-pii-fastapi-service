import logging
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from app.config import settings

logger = logging.getLogger("language_client")

credential = AzureKeyCredential(settings.AZURE_LANGUAGE_KEY)

client = TextAnalyticsClient(
    endpoint=settings.AZURE_LANGUAGE_ENDPOINT,
    credential=credential
)

def detect_pii(text: str):
    logger.info("Calling Azure PII detection")
    
    response = client.recognize_pii_entities([text])[0]
    logger.info(f"Azure returned {len(response.entities)} PII entities")

    pii_items = []

    for entity in response.entities:
        pii_items.append({
            "text": entity.text,
            "category": entity.category,
            "confidence": entity.confidence_score
        })

    return pii_items


def extract_key_phrases(text: str):
    logger.info("Calling Azure Key Phrase Extraction")

    response = client.extract_key_phrases([text])[0]
    logger.info(f"Azure returned {len(response.key_phrases)} key phrases")

    return response.key_phrases
