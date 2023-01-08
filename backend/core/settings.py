import os
from functools import lru_cache
from pydantic import BaseConfig


class Settings(BaseConfig):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///app.sqlite")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mega-secret-key")
    JWT_ALGORITHM = "HS256"


@lru_cache
def get_settings() -> Settings:
    return Settings()
