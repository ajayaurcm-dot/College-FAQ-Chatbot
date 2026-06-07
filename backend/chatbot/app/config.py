from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # ---------------------------
    # App Settings
    # ---------------------------
    APP_NAME: str = "Smart Assist Chatbot"
    DEBUG: bool = True

    # ---------------------------
    # MySQL
    # ---------------------------
    MYSQL_URL: str

    # ---------------------------
    # Groq API
    # ---------------------------
    GROQ_API_KEY: str

    # ---------------------------
    # RAG Settings
    # ---------------------------
    EMBEDDING_MODEL: str = "BAAI/bge-base-en"
    RERANKER_MODEL: str = "BAAI/bge-reranker-base"

    # ---------------------------
    # LLM Settings
    # ---------------------------
    LLM_MODEL: str = "llama-3.1-8b-instant"
    TEMPERATURE: float = 0.3
    MAX_TOKENS: int = 512

    class Config:
        env_file = ".env"
        case_sensitive = True


# ---------------------------
# Cached settings instance
# ---------------------------
@lru_cache()
def get_settings():
    return Settings()


# Global usage
settings = get_settings()
print("Using DB URL:", settings.MYSQL_URL)