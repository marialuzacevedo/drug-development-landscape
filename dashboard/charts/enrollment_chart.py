import pandas as pd
import plotly.express as px


def create_enrollment_chart(engine):

    query = """
    SELECT
        phase,
        AVG(enrollment) AS average_enrollment
    FROM studies
    WHERE phase IS NOT NULL
    GROUP BY phase
    ORDER BY phase;
    """

    enrollment_df = pd.read_sql(
        query,
        engine
    )

    def clean_label(text):

        return (
            text
            .replace("_", " ")
            .title()
        )

    enrollment_df["phase"] = (
        enrollment_df["phase"]
        .apply(clean_label)
    )
    

    fig = px.bar(

        enrollment_df,

        x="phase",

        y="average_enrollment"

    )


    fig.update_layout(

        margin=dict(

            l=40,
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

        marker_color="#7CB3BF"

    )


    fig.update_xaxes(

        tickfont=dict(

            family="Manrope",

            size=12,

            color="#9CA3AF"

        )

    )


    fig.update_yaxes(

        tickfont=dict(

            family="Manrope",

            size=12,

            color="#9CA3AF"

        ),

        showgrid=True,

        gridcolor="#EEF3F7"

    )


    return fig