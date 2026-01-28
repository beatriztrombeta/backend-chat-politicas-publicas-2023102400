from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str
    EMAIL_FROM: str
    DEBUG_EMAILS: bool = False
    GEMINI_API_KEY: str
    METABASE_SITE_URL: str
    METABASE_SECRET_KEY: str
    GROQ_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
