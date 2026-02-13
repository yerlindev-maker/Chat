from uuid import uuid4

from app.domain.message import Message

class Conversation:
    def __init__(self, user_id: str):
        self.id = str(uuid4())
        self.user_id = user_id
        self._messages = []
        self.is_closed = False

    @property
    def messages(self):
        return self._messages.copy()
    
    def add_message(self, role: str, content: str):
        if self.is_closed:
            raise ValueError("Conversation is closed")
        
        message = Message(role, content)
        self._messages.append(message)

        return message
    
    def close(self):
        self.is_closed = True