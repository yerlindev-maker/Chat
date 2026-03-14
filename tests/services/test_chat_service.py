from app.schemas.chat import ChatRequest
from app.services.chat_service import process_message


# Comprueba que el servicio genera el eco esperado.
def test_process_message_returns_expected_reply():
    payload = ChatRequest(message="Hola")

    response = process_message(payload)

    assert response.reply == "RecibÃ­ tu mensaje: Hola"
