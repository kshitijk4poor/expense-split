import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Daily Expenses Sharing Application"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://user:password@db:5432/expenses_db"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
