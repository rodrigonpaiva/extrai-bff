FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_DISABLE_PIP_VERSION_CHECK=1

# deps base (curl p/ healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# dependências mínimas
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# código
COPY src ./src

EXPOSE 8000
CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8000"]