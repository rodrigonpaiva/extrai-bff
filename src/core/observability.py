from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

def setup_observability(app: FastAPI):
    try:
        Instrumentator().instrument(app).expose(app, endpoint="/metrics")
    except Exception:
        # não falhar startup por métrica
        pass