# Maneja la configuracion central de la aplicacion.
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuracion cargada desde variables de entorno o archivo .env."""

    database_url: str = "sqlite:///./chat.db"

    # Parametros de lectura de configuracion.
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="CHAT_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Retorna la instancia cacheada de configuracion."""
    return Settings()
