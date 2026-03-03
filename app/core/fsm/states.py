from dataclasses import dataclass
from enum import Enum
from typing import Optional


class StateName (Enum):
    IDLE = "IDLE"
    GREETING = "GREETING"
    MENU = "MENU"
    COLLECTING_NAME = "COLLECTING_NAME"
    COLLECTING_ID = "COLLECTING_ID"
    COLLECTING_PLACE = "COLLECTING_PLACE"
    COLLECTING_DATE = "COLLECTING_DATE"
    CONFIRMING = "CONFIRMING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    ERROR = "ERROR"

@dataclass
class State:
    name: StateName
    message: str 
    expects_input: bool = True
    is_finished: bool = False
    timeout: Optional[int] = None


STATES = {
    StateName.IDLE: State(
        name=StateName.IDLE,
        message="¡Hola! ¿En qué puedo ayudarte?",
    ),
    StateName.GREETING: State(
        name=StateName.GREETING,
        message="¡Hola!, Bienvenido",
        expects_input=False
    ),
    StateName.MENU: State(
        name=StateName.MENU,
        message="Por favor seleccione una de las siguientes opciones"
    )
}