from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class Player:
    id: int
    nombre: str
    puntaje: int = 0
    respondio: bool = False


@dataclass(frozen=True)
class GameState:
    jugadores: Tuple[Player, ...] = field(default_factory=tuple)
    pregunta_actual: int = 0
    tiempo_restante: int = 30
    ronda: int = 1
    juego_activo: bool = True