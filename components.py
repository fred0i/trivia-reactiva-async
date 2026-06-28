from reactpy import html


def titulo():
    return html.h1(
        {
            "style": {
                "textAlign": "center",
                "color": "#2c3e50",
            }
        },
        "🎮 Trivia Arena Async"
    )


def temporizador(segundos):
    return html.h2(
        {
            "style": {
                "color": "red",
                "textAlign": "center"
            }
        },
        f"⏳ Tiempo restante: {segundos} s"
    )


def pregunta(texto):
    return html.div(
        html.h3("Pregunta"),
        html.p(texto)
    )


def opciones():
    return html.div(
        html.button("A"),
        html.button("B"),
        html.button("C"),
        html.button("D"),
    )


def jugadores(lista):

    return html.div(

        html.h3("Jugadores"),

        html.ul(

            *[
                html.li(
                    f"{j.nombre} - {j.puntaje} puntos"
                )

                for j in lista
            ]

        )

    )