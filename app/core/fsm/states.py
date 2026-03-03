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
    timeout: Optional[int]

STATES = {}