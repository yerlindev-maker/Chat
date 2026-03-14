# Configura la conexion a base de datos y fabrica de sesiones.
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config.settings import get_settings

settings = get_settings()
DATABASE_URL = settings.database_url

# Crea el engine con opciones especiales para SQLite.
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)

# Sesiones listas para inyeccion en servicios.
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    # Base comun para los modelos ORM.
    pass
