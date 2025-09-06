from fastapi import FastAPI
from src.core.observability import setup_observability
from src.core.logging import setup_logging
from src.core.config import settings
from src.routers import health, auth, analytics, groups

def create_app() -> FastAPI:
    setup_logging(level=settings.LOG_LEVEL)
    app = FastAPI(
        title="Extrai BFF API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    setup_observability(app)

    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
    app.include_router(groups.router, prefix="/groups", tags=["groups"])

    return app