from fastapi import FastAPI
from src.routers import health

def create_app() -> FastAPI:
    app = FastAPI(
        title="Extrai BFF API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )
    app.include_router(health.router, prefix="/health", tags=["health"])
    return app