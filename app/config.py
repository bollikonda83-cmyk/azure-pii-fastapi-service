import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AZURE_LANGUAGE_ENDPOINT = os.getenv("AZURE_LANGUAGE_ENDPOINT")
    AZURE_LANGUAGE_KEY = os.getenv("AZURE_LANGUAGE_KEY")

settings = Settings()

AZURE_TRANSLATOR_ENDPOINT: str
AZURE_TRANSLATOR_KEY: str
AZURE_TRANSLATOR_REGION: str

