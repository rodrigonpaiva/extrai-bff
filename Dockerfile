# ===== Base (common) =====
FROM python:3.11-slim AS base

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  PIP_DISABLE_PIP_VERSION_CHECK=1

# dependências do sistema (curl p/ healthcheck, build-essential se precisar)
RUN apt-get update && apt-get install -y --no-install-recommends \
  curl build-essential \
  && rm -rf /var/lib/apt/lists/*

# dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ===== Dev =====
FROM base AS dev
RUN pip install --no-cache-dir watchfiles
COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# ===== Prod =====
FROM base AS prod
# cria usuário não-root por segurança
RUN addgroup --system app && adduser --system --ingroup app app
USER app

COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
