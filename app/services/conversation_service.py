from datetime import datetime
from typing import Dict
from uuid import uuid4

from app.models import conversation
from app.models.message import Message


class ConversationService:
    def __init__(self):
        self._conversations = {}
    
    def create(self, user_id):
        #Generar el id
        new_id = str(uuid4())

        #Crear objeto Conversation
        conversation = conversation.Conversation(
            conversation_id=new_id,
            user_id=user_id
        )

        self._conversations[new_id] = conversation
        return conversation

    def get(self, conversation_id, user_id):
        if conversation_id and conversation_id in self._conversations:
            return self._conversations[conversation_id]
        else:
            return self.create(user_id)
        
    def add_message(self, conversation_id, user_id, role, content):
        self.get(conversation_id, user_id)
        
        message = Message(
            role=role,
            content=content,
            timestamp=datetime
        )
        
        conversation.m