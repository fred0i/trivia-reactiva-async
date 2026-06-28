# Trivia Arena Async

Proyecto desarrollado en Python utilizando ReactPy y Asyncio.

## Integrantes

- Freddy Lainez
- Jose
- Carlos
- Jonathan Panchana Rodríguez

## Tecnologías

- Python 3.x
- ReactPy
- Asyncio
- SQLite (aiosqlite)

## Arquitectura

El proyecto utiliza programación funcional con un estado global inmutable.

La lógica del juego se basa en una función pura:

update(estado_actual, accion) -> nuevo_estado

## Módulos

- state.py: Estado global del juego.
- actions.py: Acciones del sistema.
- reducer.py: Actualización funcional del estado.
- questions.py: Banco de preguntas.
- tasks.py: Corrutinas automáticas.
- database.py: Persistencia asíncrona.
- components.py: Interfaz ReactPy.