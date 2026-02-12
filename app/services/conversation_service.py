from sqlalchemy import select
from app.db.database import SessionLocal
from app.models.conversation import Conversation
from app.models.message import Message
from uuid import uuid4



class ConversationService:
    def create(self, user_id: str) -> Conversation:
        with SessionLocal() as session:
            conversation = Conversation(
                id=str(uuid4()),
                user_id=user_id
            )

            session.add(conversation)
            session.commit()
            session.refresh(conversation)

            return conversation