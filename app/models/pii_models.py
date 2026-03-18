from pydantic import BaseModel
from typing import List, Dict

class PIIRequest(BaseModel):
    text: str

class PIIResponse(BaseModel):
    pii: List[Dict]

class KeyPhraseRequest(BaseModel):
    text: str

class KeyPhraseResponse(BaseModel):
    key_phrases: List[str]
