# Logica simple para responder mensajes entrantes.
from app.schemas.chat import ChatRequest, ChatResponse


def process_message(payload: ChatRequest):
    # Arma una respuesta eco para confirmar recepcion.
    reply_text = f"RecibÃ­ tu mensaje: {payload.message}"

    # Devuelve el esquema de respuesta esperado por la API.
    return ChatResponse(
        reply=reply_text,
        user_id=payload.user_id
    )
