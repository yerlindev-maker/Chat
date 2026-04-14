# Tabla de transiciones pendiente de definicion para la FSM.

from dataclasses import dataclass
from typing import Callable, Optional
from app.core.fsm.states import StateName
from datetime import datetime

@dataclass
class Transition:
    from_state: StateName
    condition: Callable[[str], bool]
    to_state: StateName
    error_message: Optional[str] = None
    priority: int = 100

#Funciones de condición

#IDLE
def start_chat (user_input: str):
    return True

#MENU
def option_1(user_input: str):
    return user_input == "1"

def option_2(user_input: str):
    return user_input == "2"

def option_3(user_input: str):
    return user_input == "3"

#COLLECTING_NAME
def validate_name(user_input: str):
    try:
        int(user_input)
        return False
    except ValueError:
        return True
    
#COLLECTING_ID
def validate_id (user_input: str):
    try:
        int(user_input)
        cantidad = len(user_input)
        return 6 <= cantidad <= 10
    except ValueError:
        return False
    
#COLLECTING_PLACE
def validate_place (user_input: str):
    try:
        option = int(user_input) #Guarda el valor int 
        return option > 0
    except ValueError:
        return False
    
#COLLECTING_DATE
def validate_date (user_input: str):
    try:
        fecha_cita = datetime.strptime(user_input, "%d/%m/%Y %H:%M")
        fecha_actual = datetime.now()
        return fecha_cita > fecha_actual
    except ValueError:
        return False
    
#CONFIRMING
#Confirmación del usuario
def user_confirms(user_input: str):
    return user_input.lower() in ["si", "sí", "yes" "confirmo"]

#Cancelación del usuario
def user_cancels(user_input: str):
    return user_input.lower() in ["no", "cancelar", "nop"]

#TRANSITIONS
TRANSITIONS=[    
    Transition(
        from_state=StateName.IDLE,
        condition=start_chat,
        to_state=StateName.GREETING
    ),
    Transition(
        from_state=StateName.GREETING,
        to_state=StateName.MENU
    ),
    Transition(
        from_state=StateName.MENU,
        condition=option_1,
        to_state=StateName.COLLECTING_NAME
    ),
    Transition(
        from_state=StateName.MENU,
        condition=option_2,
        to_state=StateName.COLLECTING_ID
    ),
    Transition(
        from_state=StateName.MENU,
        condition=option_3,
        to_state=StateName.COLLECTING_ID
    ),
    Transition(
        from_state=StateName.COLLECTING_NAME,
        condition=validate_name,
        error_message="Nombre inválido"
        to_state=StateName.COLLECTING_ID
    ),
    Transition(
        from_state=StateName.COLLECTING_ID,
        condition=validate_id,
        to_state=StateName.COLLECTING_PLACE
    ),
    Transition(
        from_state=StateName.COLLECTING_PLACE,
        condition=validate_place,
        to_state=StateName.COLLECTING_DATE
    ),
    Transition(
        from_state=StateName.COLLECTING_DATE,
        condition=validate_date,
        to_state=StateName.CONFIRMING
    ),
    Transition(
        from_state=StateName.CONFIRMING,
        condition=user_confirms,
        to_state=StateName.CONFIRMED
    ),
    Transition(
        from_state=StateName.CONFIRMING,
        condition=user_cancels,
        to_state=StateName.CANCELLED
    ),
    Transition(
        from_state=StateName.CONFIRMED,
        to_state=StateName.MENU
    ),
    Transition(
        from_state=StateName.CANCELLED,
        to_state=StateName.MENU
    ),
    Transition(
        from_state=StateName.ERROR,
        to_state=StateName.MENU
    )
]