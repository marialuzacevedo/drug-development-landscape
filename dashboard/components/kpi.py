from dash import html


def kpi_card(value, title):

    return html.Div(

        [

            html.H2(
                value,
                id=f"{title}-value",
                className="kpi-number"

            ),
            html.H3(title, className="kpi-title")

        ],

        className="kpi-card"

    ) 