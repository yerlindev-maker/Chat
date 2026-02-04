from app.schemas.chat import ChatRequest, ChatResponse

def process_message(payload: ChatRequest):
    reply_text = f"Recibí tu mensaje: {payload.message}"

    return ChatResponse(
        reply=reply_text,
        user_id=payload.user_id
    )
