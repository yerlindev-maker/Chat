from datetime import datetime
from uuid import uuid4
from typing import Dict

from app.models.conversation import Conversation
from app.models.message import Message


class ConversationService:
    def __init__(self):
        self._conversations: Dict[str, Conversation] = {}
    
    def create(self, user_id: str) -> Conversation:
        #Generar el id
        new_id = str(uuid4())

        #Crear objeto Conversation
        conversation = Conversation(
            conversation_id=new_id,
            user_id=user_id,
            messages=[]
        )

        self._conversations[new_id] = conversation
        return conversation

    def get(self, conversation_id: str | None, user_id: str) -> Conversation:
        #Si el id existe y está registrado, devolver la conversación
        if conversation_id and conversation_id in self._conversations:
            return self._conversations[conversation_id]
        
        #Si no existe o es None, crear una nueva
        return self.create(user_id)
        
    def add_message(
        self,
        conversation_id: str | None,
        user_id: str,
        role: str,
        content: str
    ) -> Message:
        conversation = self.get(conversation_id, user_id)

        message = Message(
            role=role,
            content=content,
            timestamp=datetime.utcnow()
        )

        conversation.messages.append(message)

        return message