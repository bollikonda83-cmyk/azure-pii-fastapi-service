import logging
from azure.ai.textanalytics import TextAnalyticsClient, ExtractSummaryAction
from azure.core.credentials import AzureKeyCredential
from app.config import settings
import requests
import logging
from app.config import settings
import os

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

def detect_language(text: str):
    logger.info("Calling Azure Language Detection")

    response = client.detect_language([text])[0]

    language = response.primary_language.name
    score = response.primary_language.confidence_score

    logger.info(f"Detected language: {language} (confidence={score})")

    return {
        "language": language,
        "confidence_score": score
    }
logger = logging.getLogger("translation_client")

def translate_text(text: str, to_language: str):
    logger.info(f"Calling Azure Translator to translate text to '{to_language}'")

    endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
    key = os.getenv("AZURE_TRANSLATOR_KEY")
    region = os.getenv("AZURE_TRANSLATOR_REGION")

    url = f"{endpoint}/translate?api-version=3.0&to={to_language}"

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-Type": "application/json"
    }

    body = [{"text": text}]

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()

    translated_text = response.json()[0]["translations"][0]["text"]

    logger.info("Translation completed successfully")

    return translated_text

def extractive_summary(text):
    poller = client.begin_analyze_actions(
        [text],
        actions=[ExtractSummaryAction(max_sentence_count=3)]
    )
    result = list(poller.result())[0][0].extract_summary_result
    return [sentence.text for sentence in result.sentences]


