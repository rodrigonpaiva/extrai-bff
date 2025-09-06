# extrai-bff

## Requisitos
- Python 3.11+
- Docker (dev opcional)

## Setup local
```bash
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make dev        # API em http://localhost:8000
make worker     # Celery worker
make beat       # Celery beat (scheduler)