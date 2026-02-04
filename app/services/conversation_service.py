from typing import Dict
from datetime import datetime
from uuid import uuid4

from app.models.conversation import Conversation, Message

class ConversationService:
    def __init__(self):
        self._conversations: Dict[str, Conversation] = {}

    def get_or_create(self, conversation_id: str | None) -> Conversation:
        if conversation_id and conversation_id in self._conversations:
            return self._conversations[conversation_id]
        
        new_id = conversation_id or str(uuid4())
        conversation = Conversation(id=new_id, message=[])
        self._conversations[new_id] = conversation 
        return conversation
    
    def add_message(self, conversation: Conversation, role: str, content: str):
        conversation.messages.append(
            Message(
                role=role,
                content=content,
                timestamp=datetime.utcnow()
            )
        )

    def get_history(self, conversation: Conversation):
        return conversation.messages