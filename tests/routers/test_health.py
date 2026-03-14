from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Valida que el endpoint de salud responda correctamente.
def test_health_endpoint_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }
