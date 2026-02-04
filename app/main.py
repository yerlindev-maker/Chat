from fastapi import FastAPI
from app.routers import health, chat

app = FastAPI(
    title="Chat API",
    version="1.0.0",
    description="API backend for chat system"
)

app.include_router(health.router)
app.include_router(chat.router)