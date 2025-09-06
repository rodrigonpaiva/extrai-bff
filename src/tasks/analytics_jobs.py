from .celery_app import celery_app

@celery_app.task(name="analytics.compute_daily_metrics")
def compute_daily_metrics():
    # TODO: job real de agregação/ETL
    return {"status": "ok"}