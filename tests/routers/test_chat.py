from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_message_endpoint():
    response = client.post(
        "/chat/message",
        json={"message": "Hola"}
    )

    assert response.status_code == 200
    assert response.json() == {
    "reply": "Recibí tu mensaje: Hola",
    "user_id": None
}
