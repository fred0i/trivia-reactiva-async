from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from state import GameState, Player
from components import (
    titulo,
    temporizador,
    pregunta,
    opciones,
    jugadores,
)

app = FastAPI()


@component
def App():

    estado = GameState(
        jugadores=(
            Player(1, "Jose", 30),
            Player(2, "Carlos", 20),
            Player(3, "Freddy", 10),
        )
    )

    return html.div(
    {"style": PAGE},

    titulo(),

    temporizador(estado.tiempo_restante),

    pregunta(
        "¿Qué librería permite programación asíncrona en Python?"
    ),

    opciones(),

    jugadores(estado.jugadores),

    html.h2(f"Ronda {estado.ronda}")
)


configure(app, App)