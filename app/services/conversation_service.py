from typing import Dict
from datetime import datetime
from uuid import uuid4

from app.models.conversation import Conversation, Message

class ConversationService:
    def __init__(self):
        #Diccionario que almacena todas las conversaciones en memoria
        #La clave es conversation_id
        #El valor es un objeto Conversation
        self._conversations = {}

    def get_or_create(self, conversation_id):
        """
        Devuelve una conversación existente si el ID ya existe.
        Si no existe, crea una nueva conversación.
        """
        #Caso 1: El cliente envía conversation_id
        if conversation_id is not None:
            #Si ya existe, la devolvemos
            if conversation_id in self._conversations:
                return self._conversations[conversation_id]
            
            #Si no existe, creamos una nueva con ese mismo ID
            new_id = conversation_id
        else:
            #Caso 2: El cliente NO envía ID -> generamos uno nuevo
            new_id = str(uuid4())

        #crear una conversación vacía
        conversation = Conversation(
            id=new_id,
            messages=[]
        )

        #Guardarla en memoria
        self._conversations[new_id] = conversation

        return conversation

    def add_message(self, conversation, role, content):
        """
        Agrega un mensaje a una conversación existente
        """

        message = Message(
            role=role,
            content=content,
            timestamp=datetime.utcnow()
        )

        conversation.messages.append(message)

    def get_history(self, conversation):
        """
        Devuelve el historial completo de mensajes de una conversación.
        """
        return conversation.messages
    