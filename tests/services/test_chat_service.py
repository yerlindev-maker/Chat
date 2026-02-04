from app.schemas.chat import ChatRequest
from app.services.chat_service import process_message

def test_process_message_returns_expected_reply():
    payload = ChatRequest(message="Hola")

    response = process_message(payload)

    assert response.reply == "Recibí tu mensaje: Hola"