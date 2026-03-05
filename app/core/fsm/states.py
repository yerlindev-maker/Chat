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
        message="Por favor seleccione una de las siguientes opciones: "
    ),
    StateName.COLLECTING_NAME: State(
        name=StateName.COLLECTING_NAME,
        message="Por favor ingrese el nombre de la persona a la cuál se le agendará la cita: "
    ),
    StateName.COLLECTING_ID: State(
        name=StateName.COLLECTING_NAME,
        message="Por favor ingrese el número de identificación de la persona: "
    ),
    StateName.COLLECTING_PLACE: State(
        name=StateName.COLLECTING_PLACE,
        message="Por favor escoja la sede: "
    ),
    StateName.COLLECTING_DATE: State(
        name=StateName.COLLECTING_DATE,
        message="Escoja alguna de las fechas disponibles: "
    )

    
}