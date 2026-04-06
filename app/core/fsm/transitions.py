# Tabla de transiciones pendiente de definicion para la FSM.

from dataclasses import dataclass
from typing import Callable, Optional
from app.core.fsm.states import StateName
from states import STATES
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
def option_select(option: str):
    options = ["1", "2", "3"]
    return option in options    

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
    return user_input.lower in ["si", "sí", "yes" "confirmo"]

#Cancelación del usuario
def user_cancels(user_input: str):
    return user_input.lower() in ["no", "cancelar", "nop"]