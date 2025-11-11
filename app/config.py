from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware

class Settings(BaseSettings):
    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_DSN: str
    FRONTEND_URL: str = "http://localhost:5173"
    JWT_SECRET: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.FRONTEND_URL, "*"],  # ajuste em produção
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
