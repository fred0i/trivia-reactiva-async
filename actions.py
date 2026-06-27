from dataclasses import dataclass


@dataclass(frozen=True)
class RegistrarJugador:
    id: int
    nombre: str


@dataclass(frozen=True)
class ResponderPregunta:
    jugador_id: int
    opcion: str
    respuesta_correcta: str


@dataclass(frozen=True)
class ReducirTiempo:
    cantidad: int = 1


@dataclass(frozen=True)
class CerrarRonda:
    motivo: str


@dataclass(frozen=True)
class NuevaRonda:
    tiempo_inicial: int = 30


@dataclass(frozen=True)
class FinalizarJuego:
    motivo: str