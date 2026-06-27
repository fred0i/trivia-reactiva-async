from dataclasses import replace

from state import GameState, Player
from actions import (
    RegistrarJugador,
    ResponderPregunta,
    ReducirTiempo,
    CerrarRonda,
    NuevaRonda,
    FinalizarJuego,
)


def update(estado: GameState, accion):

    if isinstance(accion, RegistrarJugador):

        nuevo_jugador = Player(
            id=accion.id,
            nombre=accion.nombre
        )

        return replace(
            estado,
            jugadores=estado.jugadores + (nuevo_jugador,)
        )

    if isinstance(accion, ResponderPregunta):

        jugadores = []

        for jugador in estado.jugadores:

            if jugador.id == accion.jugador_id:

                correcto = accion.opcion == accion.respuesta_correcta

                jugadores.append(
                    replace(
                        jugador,
                        puntaje=jugador.puntaje + (10 if correcto else 0),
                        respondio=True
                    )
                )

            else:

                jugadores.append(jugador)

        return replace(
            estado,
            jugadores=tuple(jugadores)
        )

    if isinstance(accion, ReducirTiempo):

        return replace(
            estado,
            tiempo_restante=max(
                0,
                estado.tiempo_restante - accion.cantidad
            )
        )

    if isinstance(accion, CerrarRonda):

        return replace(
            estado,
            juego_activo=False
        )

    if isinstance(accion, NuevaRonda):

        jugadores = tuple(
            replace(jugador, respondio=False)
            for jugador in estado.jugadores
        )

        return replace(
            estado,
            ronda=estado.ronda + 1,
            pregunta_actual=estado.pregunta_actual + 1,
            tiempo_restante=accion.tiempo_inicial,
            jugadores=jugadores,
            juego_activo=True
        )

    if isinstance(accion, FinalizarJuego):

        return replace(
            estado,
            juego_activo=False
        )

    return estado