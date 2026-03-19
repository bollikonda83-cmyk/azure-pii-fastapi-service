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

logger = logging.getLogger("translation_client")

def classify_text(text: str):
    logger.info("Calling Azure Sentiment Analysis for text classification")

    response = client.analyze_sentiment([text])[0]

    sentiment = response.sentiment  # "positive", "neutral", or "negative"
    scores = response.confidence_scores

    logger.info(
        f"Classification result: {sentiment} "
        f"(pos={scores.positive}, neu={scores.neutral}, neg={scores.negative})"
    )

    return {
        "label": sentiment,
        "positive_score": scores.positive,
        "neutral_score": scores.neutral,
        "negative_score": scores.negative,
    }



