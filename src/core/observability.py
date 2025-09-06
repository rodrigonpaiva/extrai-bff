# src/core/observability.py
import logging
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

logger = logging.getLogger(__name__)


def setup_observability(app: FastAPI):
    try:
        Instrumentator().instrument(app).expose(app, endpoint="/metrics")
    except Exception as exc:
        logger.warning("Prometheus instrumentation disabled: %s", exc)
