from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "AstroShot Planner API"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/astroshot"
    cors_origins: list[str] = Field(default=["http://localhost:3000"], alias="BACKEND_CORS_ORIGINS")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
