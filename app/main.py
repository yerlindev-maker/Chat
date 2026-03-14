# App principal de FastAPI donde se ensamblan los routers.
from fastapi import FastAPI
from app.routers import health, chat

# Importa modelos y crea las tablas en el arranque para evitar migraciones manuales.
from app.db.database import Base, engine
from app.models import conversation, message

Base.metadata.create_all(bind=engine)

# Configuracion basica de la API.
app = FastAPI(
    title="Chat API",
    version="1.0.0",
    description="API backend para el sistema de chat"
)

# Registra los endpoints disponibles.
app.include_router(health.router)
app.include_router(chat.router)
