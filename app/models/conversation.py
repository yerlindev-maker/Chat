# Modelo ORM para conversaciones de usuario.
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean
from typing import List
from uuid import uuid4

from app.db.database import Base
from app.models.message import Message


class Conversation(Base):
    __tablename__ = "conversations"

    # Identificador unico generado como UUID en texto.
    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    # Usuario propietario de la conversacion.
    user_id: Mapped[str] = mapped_column(String, nullable=False)

    # Indica si ya no admite mensajes nuevos.
    is_closed: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    # Relacion con los mensajes, cascada para eliminarlos juntos.
    messages: Mapped[List["Message"]] = relationship(
        back_populates="conversation",
        cascade="all, delete-orphan"
    )

    def add_message(self, role: str, content: str) -> Message:
        # Validaciones basicas antes de crear el mensaje.
        if self.is_closed:
            raise ValueError("Conversation is closed")

        if not content.strip():
            raise ValueError("Message content cannot be empty")

        if role not in ("user", "assistant"):
            raise ValueError("Invalid role")

        # Instancia y vincula el mensaje a la conversacion.
        message = Message(
            role=role,
            content=content,
            conversation=self
        )

        self.messages.append(message)

        return message

    def close(self) -> None:
        # Marca la conversacion como cerrada.
        self.is_closed = True
