import logging
from fastapi import APIRouter
from app.models.pii_models import (
    PIIRequest, PIIResponse,
    KeyPhraseRequest, KeyPhraseResponse, TranslationResponse
)
from app.pii_client import detect_pii, extract_key_phrases

logger = logging.getLogger("pii_router")

router = APIRouter(prefix="/pii", tags=["PII Detection & Language"])

from app.models.pii_models import (
    PIIRequest, PIIResponse,
    KeyPhraseRequest, KeyPhraseResponse,
    TranslationRequest, TranslationResponse,
    ClassificationRequest, ClassificationResponse,
)
from app.pii_client import (
    detect_pii,
    extract_key_phrases,
    classify_text,
)
from app.models.pii_models import (
    PIIRequest, PIIResponse,
    KeyPhraseRequest, KeyPhraseResponse,
    TranslationRequest, TranslationResponse,
    ClassificationRequest, ClassificationResponse,
    LanguageDetectionRequest, LanguageDetectionResponse
)

from app.pii_client import (
    detect_pii,
    extract_key_phrases,
    classify_text,
    detect_language
)

from app.models.pii_models import (
    TranslationRequest, TranslationResponse
)
from app.pii_client import translate_text


@router.post("/", response_model=PIIResponse)
def pii_detection(req: PIIRequest):
    logger.info("PII detection endpoint called")
    result = detect_pii(req.text)
    logger.info("PII detection completed")
    return PIIResponse(pii=result)


@router.post("/keyphrases", response_model=KeyPhraseResponse)
def key_phrase_extraction(req: KeyPhraseRequest):
    logger.info("Key phrase extraction endpoint called")
    result = extract_key_phrases(req.text)
    logger.info("Key phrase extraction completed")
    return KeyPhraseResponse(key_phrases=result)

@router.post("/classify", response_model=ClassificationResponse)
def classify(req: ClassificationRequest):
    logger.info("Text classification endpoint called")
    result = classify_text(req.text)
    logger.info("Text classification completed")
    return ClassificationResponse(**result)

@router.post("/language", response_model=LanguageDetectionResponse)
def language_detection(req: LanguageDetectionRequest):
    logger.info("Language detection endpoint called")
    result = detect_language(req.text)
    logger.info("Language detection completed")
    return LanguageDetectionResponse(**result)

@router.post("/translate", response_model=TranslationResponse)
def translate(req: TranslationRequest):
    logger.info("Translation endpoint called")
    result = translate_text(req.text, req.to_language)
    logger.info("Translation completed")
    return TranslationResponse(translated_text=result)
