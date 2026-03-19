from pydantic import BaseModel
from typing import List, Dict
from pydantic import BaseModel
from typing import List, Optional

class PIIRequest(BaseModel):
    text: str

class PIIResponse(BaseModel):
    pii: List[Dict]

class KeyPhraseRequest(BaseModel):
    text: str

class KeyPhraseResponse(BaseModel):
    key_phrases: List[str]

class TranslationRequest(BaseModel):
    text: str
    to_language: str

class TranslationResponse(BaseModel):
    translated_text: str

class ClassificationRequest(BaseModel):
    text: str

class ClassificationResponse(BaseModel):
    label: str
    positive_score: float
    neutral_score: float
    negative_score: float

