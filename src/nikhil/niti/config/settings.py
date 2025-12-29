import os

from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_CONFIG: str | None = os.getenv("APP_CONFIG")
    LLM_CONFIG: str | None = os.getenv("LLM_CONFIG")
