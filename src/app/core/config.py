from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from typing import Any, Dict, List, Optional, Union


class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "Base fastapi project"


settings = Settings()
