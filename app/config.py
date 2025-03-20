from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://wassup:homie@db/fastapi_app"
    SECRET_KEY: str = "your-secret-key-keep-this-secure-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    CACHE_EXPIRY_SECONDS: int = 300

settings = Settings()
