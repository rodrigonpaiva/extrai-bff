# ⚡ Extrai BFF

[![CI](https://github.com/YOUR-USER/extrai-bff/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR-USER/extrai-bff/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Extrai BFF** is a **FastAPI + Celery backend** that acts as an **orchestrator** between:

- 📊 Database (Postgres)  
- ⚡ Asynchronous processing queue (Celery + Redis)  
- 🤖 AI analysis services (OpenAI API)  
- 🖥️ Web Dashboard (Next.js)  

---

## 🚀 Tech Stack

- **FastAPI** – main REST API  
- **Celery + Redis** – async tasks & daily schedulers  
- **PostgreSQL** – data persistence  
- **SQLAlchemy** – ORM / data access layer  
- **Prometheus + OpenTelemetry** – observability  
- **Docker / Compose** – local environment & deployment  

---

## 📂 Project Structure

```
extrai-bff/
├─ src/
│  ├─ app.py           # FastAPI factory
│  ├─ main.py          # entrypoint
│  ├─ core/            # config, logging, observability, security
│  ├─ adapters/        # db, redis, external clients
│  ├─ routers/         # REST endpoints
│  ├─ services/        # business logic
│  ├─ tasks/           # celery jobs & scheduler
│  └─ schemas/         # DTOs (Pydantic)
├─ docs/               # openapi.yaml, ADRs
├─ infra/              # docker, k8s, terraform
├─ tests/              # unit/integration tests
```

---

## ⚙️ Getting Started

### Local (without Docker)

```bash
# 1. Clone the repository
git clone git@github.com:YOUR-USER/extrai-bff.git
cd extrai-bff
```

# 2. Create and activate virtualenv

```
python -m venv .venv && source .venv/bin/activate
```

# 3. Install dependencies

```
pip install -r requirements.txt
```

# 4. Copy env

```
cp .env.example .env
```

# 5. Run API

```
make dev
```

API available at: <http://localhost:8000/docs>

⸻

Local (with Docker Compose)

```
cp .env.example .env
docker compose up -d --build
```

Services:
 • API → <http://localhost:8000>
 • Postgres → localhost:5432
 • Redis → localhost:6379

⸻

Celery Tasks

```
# Worker
make worker

# Scheduler (beat)
make beat
```

⸻

🧪 Testing

```
pytest -q
```

⸻

🔍 Observability
 • Healthcheck: /health
 • OpenAPI: /docs and /openapi.json
 • Prometheus metrics: /metrics
 • Tracing: via OpenTelemetry (OTEL_EXPORTER_OTLP_ENDPOINT)

⸻

📦 CI/CD
 • CI: linting, tests, Docker build (GitHub Actions)
 • CD: optional via VPS (Docker Compose) or Kubernetes (manifests in infra/k8s)

⸻

📝 License

This project is licensed under MIT.

