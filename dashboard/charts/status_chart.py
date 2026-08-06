import pandas as pd
import plotly.express as px


def create_status_chart(engine):

    query = """
    SELECT
        status,
        COUNT(study_id) AS number_of_trials
    FROM studies
    GROUP BY status
    ORDER BY number_of_trials DESC;
    """

    status_df = pd.read_sql(
        query,
        engine
    )

    def clean_label(text):

        return (
            text
            .replace("_", " ")
            .title()
        )

    status_df["status"] = (
        status_df["status"]
        .apply(clean_label)
    )

    fig = px.bar(

        status_df,

        x="number_of_trials",

        y="status",

        orientation="h"

    )


    fig.update_layout(

        margin=dict(

            l=110,

            r=20,

            t=20,

            b=40

        ),

        height=450,

        showlegend=False,

        xaxis_title=None,

        yaxis_title=None

    )


    fig.update_traces(

        marker_color="#337687"

    )


    fig.update_yaxes(

        categoryorder="total ascending",

        tickfont=dict(

            family="Manrope",

            size=11,

            color="#9CA3AF"

        ),

        showgrid=False,

        zeroline=False,

        autorange="reversed"

    )


    fig.update_xaxes(

        tickfont=dict(

            family="Manrope",

            size=12,

            color="#9CA3AF"

        )

    )


    return fig