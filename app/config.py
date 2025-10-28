from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
