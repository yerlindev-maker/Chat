from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables or .env."""

    database_url: str = "sqlite:///./chat.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="CHAT_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
