from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import List
from uuid import uuid4

from app.db.database import Base
from app.models.message import Message

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(String, nullable=False)

    is_closed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    messages: Mapped[List["Message"]] = relationship(
        back_populates="conversation",
        cascade="all, delete_orphan"
    )

    def add_message(self, role: str, content: str) -> Message:
        if self.is_closed:
            raise ValueError("Conversation is closed")

        if not content.strip():
            raise ValueError("Message content cannot be empty")
        
        if role not in("user", "asistent"):
            raise ValueError("Invalid role")
        
        message = Message(
            role=role,
            content=content,
            conversation=self
        )

        self.messages.append(message)
        return message
    
    def close(self) -> None:
        self.is_closed = True