from datetime import datetime

class Message:
    def __init__(self, role: str, content: str):
        if not content.strip():
            raise ValueError("Message content cannot be empty")
        
        if role not in("user", "assistant"):
            raise ValueError("Invalid role")
        
        self.role = role
        self.content = content
        self.timestamp = datetime.utcnow()