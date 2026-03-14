# Motor que ejecutara la maquina de estados; aun sin implementar.

from dataclasses import dataclass
from typing import Callable
from app.core.fsm.states import StateName

@dataclass
class Transition:
    from_state: StateName
    condition: Callable[[str], bool]
    to_state: StateName