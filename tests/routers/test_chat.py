from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Comprueba la respuesta del endpoint de mensajes de chat.
def test_chat_message_endpoint():
    response = client.post(
        "/chat/message",
        json={"message": "Hola"}
    )

    assert response.status_code == 200
    assert response.json() == {
    "reply": "RecibÃ­ tu mensaje: Hola",
    "user_id": None
}
