from typing import List
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl

class Settings(BaseSettings):
    PROJECT_NAME: str = "LogiTrans"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here"  # Change this in production!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:8090",
        "http://localhost:8080",
        "http://localhost:3000",
        "http://localhost"
    ]
    
    # Database
    DATABASE_URL: str = "sqlite:///./sql_app.db"
    
    class Config:
        case_sensitive = True

settings = Settings()
