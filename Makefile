.PHONY: dev test lint fmt up down worker beat

dev:           ## run api in dev (reload)
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

worker:        ## run celery worker
	celery -A src.tasks.celery_app.celery_app worker -Q default -l info

beat:          ## run scheduler (periodic tasks)
	celery -A src.tasks.celery_app.celery_app beat -l info

test:
	pytest -q

lint:
	ruff check src tests

fmt:
	ruff check --fix src tests && ruff format src tests

up:
	docker compose up -d --build

down:
	docker compose down