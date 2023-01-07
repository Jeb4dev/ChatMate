import os
from functools import lru_cache
from pydantic import BaseConfig


class Settings(BaseConfig):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///app.sqlite")


@lru_cache
def get_settings() -> Settings:
    return Settings()
