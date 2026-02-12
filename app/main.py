from fastapi import FastAPI
from app.routers import health, chat

from app.db.database import Base, engine
from app.models import conversation, message

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chat API",
    version="1.0.0",
    description="API backend for chat system"
)

app.include_router(health.router)
app.include_router(chat.router)