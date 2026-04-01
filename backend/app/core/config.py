from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "AstroShot Planner API"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/astroshot"
    cors_origins: list[str] | str = Field(default="http://localhost:3000", validation_alias="BACKEND_CORS_ORIGINS")

    @field_validator("cors_origins", mode="before")
    @classmethod
    def split_cors_origins(cls, value: list[str] | str) -> list[str]:
        if isinstance(value, list):
            return value
        return [item.strip() for item in value.split(",") if item.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
