from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_ENV: str = "dev"
    APP_PORT: int = 8000
    LOG_LEVEL: str = "INFO"

    POSTGRES_URL: str
    REDIS_URL: str

    JWT_SECRET: str
    JWT_ISSUER: str = "extrai"
    JWT_AUDIENCE: str = "dashboard"

    OPENAI_API_KEY: str | None = None
    RATE_LIMIT_OPENAI_RPM: int = 60

    PROMETHEUS_METRICS: bool = True
    OTEL_EXPORTER_OTLP_ENDPOINT: str | None = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
