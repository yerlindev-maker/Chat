# Esquemas Pydantic para validar entradas y salidas del chat.
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str 
    user_id: str
    conversation_id: Optional[str] = None
    timestamp: Optional[datetime] = None


class ChatResponse(BaseModel):
    reply: str
    user_id: str
    conversation_id: Optional[str] = None
    timestamp: Optional[datetime] = None
