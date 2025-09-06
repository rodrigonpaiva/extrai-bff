from .celery_app import celery_app

celery_app.conf.beat_schedule.update(
    {
        "analytics-every-24h": {
            "task": "analytics.compute_daily_metrics",
            "schedule": 60 * 60 * 24,  # 24h
            "options": {"queue": "default"},
        }
    }
)
