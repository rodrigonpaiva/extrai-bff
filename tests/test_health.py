from fastapi.testclient import TestClient
from src.app import create_app

client = TestClient(create_app())

def test_health_endpoint_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body.get("status") == "ok"