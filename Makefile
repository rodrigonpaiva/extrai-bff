.PHONY: up up-prod down logs logs-prod build clean

# === Dev profile ===
up:
	docker compose --profile dev up -d --build
	@echo "🚀 Dev API running at: http://localhost:8000"

logs:
	docker compose logs -f api

# === Prod profile ===
up-prod:
	docker compose --profile prod up -d --build
	@echo "🚀 Prod API running at: http://localhost:8001"

logs-prod:
	docker compose logs -f api-prod

# === Common ===
down:
	docker compose down -v

build:
	docker compose build

clean:
	docker system prune -af --volumes