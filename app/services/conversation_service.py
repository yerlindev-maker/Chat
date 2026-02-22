from app.db.database import SessionLocal
from app.models.conversation import Conversation

class ConversationService:
    def create(self, user_id: str) -> Conversation:
        with SessionLocal() as session:
            conversation = Conversation(
                user_id=user_id
            )

            session.add(conversation)
            session.commit()
            session.refresh(conversation)

            return conversation