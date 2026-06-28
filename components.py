from styles import PAGE, CARD, BUTTON
from reactpy import html


def titulo():
    return html.h1(
        {
            "style": {
                "textAlign": "center",
                "color": "#1E3A8A"
            }
        },
        "🎮 Trivia Arena Async"
    )


def temporizador(segundos):
    return html.h2(
        {
            "style": {
                "color": "#DC2626",
                "textAlign": "center"
            }
        },
        f"⏳ Tiempo restante: {segundos} segundos"
    )


def pregunta(texto):
    return html.div(
        html.h2("Pregunta"),
        html.p(texto)
    )


def opciones():

    return html.div(

        html.button("A", {"style": BUTTON}),
        html.button("B", {"style": BUTTON}),
        html.button("C", {"style": BUTTON}),
        html.button("D", {"style": BUTTON}),

    )


def jugadores(lista):

    return html.div(

        html.h2("Jugadores"),

        html.table(

            html.tr(
                html.th("Jugador"),
                html.th("Puntos")
            ),

            *[
                html.tr(

                    html.td(j.nombre),
                    html.td(str(j.puntaje))

                )

                for j in lista

            ]

        )

    )