from datetime import datetime
from typing import Dict
from uuid import uuid4

from app.models.conversation import Conversation
from app.models.message import Message


class ConversationService:
    def __init__(self):
        self._conversations = {}
    
    def create(self, user_id):
        #Generar el id
        new_id = str(uuid4())

        #Crear objeto Conversation
        conversation = Conversation(
            conversation_id=new_id,
            user_id=user_id
        )

        self._conversations[new_id] = conversation
        return conversation