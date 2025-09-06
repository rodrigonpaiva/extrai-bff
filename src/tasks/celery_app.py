from celery import Celery
from src.core.config import settings

celery_app = Celery(
    "extrai",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)
celery_app.conf.update(
    task_default_queue="default",
    task_time_limit=60 * 10,
    worker_max_tasks_per_child=100,
    beat_schedule={},  # preenchido em periodic.py
)