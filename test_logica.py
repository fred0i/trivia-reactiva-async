from state import GameState
from actions import RegistrarJugador, ResponderPregunta, ReducirTiempo, NuevaRonda
from reducer import update


estado = GameState()

estado = update(estado, RegistrarJugador(1, "Freddy"))
estado = update(estado, RegistrarJugador(2, "Jose"))
estado = update(estado, RegistrarJugador(3, "Carlos"))

estado = update(estado, ResponderPregunta(1, "A", "A"))
estado = update(estado, ResponderPregunta(2, "B", "A"))
estado = update(estado, ReducirTiempo(5))

print("Jugadores:")
for jugador in estado.jugadores:
    print(jugador.nombre, jugador.puntaje, jugador.respondio)

print("Tiempo restante:", estado.tiempo_restante)
print("Ronda:", estado.ronda)

estado = update(estado, NuevaRonda())

print("Nueva ronda:", estado.ronda)
print("Tiempo reiniciado:", estado.tiempo_restante)