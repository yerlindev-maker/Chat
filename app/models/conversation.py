from dataclasses import dataclass, field
from typing import List
from .message import Message

@dataclass
class Conversation:
    conversation_id: str
    user_id: str
    messages: List[Message] = field(default_factory=list)