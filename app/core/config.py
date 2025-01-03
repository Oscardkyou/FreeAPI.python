from pydantic_settings import BaseSettings
import secrets

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "LogiTrans"
    VERSION: str = "1.0.0"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sql_app.db"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    BACKEND_CORS_ORIGINS: list = ["*"]  # In production, replace with specific origins

settings = Settings()
