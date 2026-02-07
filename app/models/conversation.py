from dataclasses import dataclass, field
from typing import List
from .message import Message


class Conversation:
    #def __init__(self, conversation_id, user_id):
     #   self.conversation_id = conversation_id
      #  self.user_id = user_id
        
    
    conversation_id: str
    user_id: str
    messages: List[Message] = field(default_factory=list)