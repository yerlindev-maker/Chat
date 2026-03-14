# Modelo ORM para los mensajes individuales.
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from datetime import datetime

from app.db.database import Base


class Message(Base):
    __tablename__ = "messages"

    # Identificador autoincremental.
    id: Mapped[int] = mapped_column(primary_key=True)

    # Clave foranea hacia la conversacion.
    conversation_id: Mapped[str] = mapped_column(
        ForeignKey("conversations.id"),
        nullable=False
    )

    # Rol del emisor y contenido plano.
    role: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    # Marca temporal asignada al crear.
    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    # Relacion inversa con la conversacion.
    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )
