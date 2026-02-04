from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_message

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/message", response_model=ChatResponse)
def send_message(payload: ChatRequest):
    return process_message(payload)