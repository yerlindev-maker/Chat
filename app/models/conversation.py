from typing import List, Literal
from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    role: Literal["user", "assistent"]
    content: str
    timestamp: datetime

class Conversation(BaseModel):
    id: str
    messages: List[Message] = []