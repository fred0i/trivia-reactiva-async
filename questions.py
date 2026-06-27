from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Question:
    texto: str
    opciones: Tuple[str, str, str, str]
    respuesta_correcta: str


QUESTIONS = (
    Question(
        texto="¿Qué librería permite manejar programación asíncrona en Python?",
        opciones=("ReactPy", "Asyncio", "SQLite", "Tkinter"),
        respuesta_correcta="Asyncio"
    ),
    Question(
        texto="¿Qué función se usa para crear tareas concurrentes en asyncio?",
        opciones=("asyncio.create_task", "print", "input", "time.sleep"),
        respuesta_correcta="asyncio.create_task"
    ),
    Question(
        texto="¿Qué concepto evita modificar directamente el estado original?",
        opciones=("Mutabilidad", "Inmutabilidad", "Bloqueo", "HTML"),
        respuesta_correcta="Inmutabilidad"
    ),
)