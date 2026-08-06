import pandas as pd
import plotly.express as px


def create_sponsor_chart(engine):

    query = """
    SELECT
        s.sponsor_name,
        COUNT(ss.study_id) AS number_of_trials
    FROM study_sponsors ss
    JOIN sponsors s
        ON ss.sponsor_id = s.sponsor_id
    GROUP BY s.sponsor_name
    ORDER BY number_of_trials DESC
    LIMIT 10;
    """

    sponsor_df = pd.read_sql(
        query,
        engine
    )

    sponsor_mapping = {

    "Novartis Pharmaceuticals": "Novartis",

    "Hoffmann-La Roche": "Roche",

    "Merck Sharp & Dohme LLC": "Merck",

    "Bristol-Myers Squibb": "Bristol Myers Squibb"

}


    sponsor_df["sponsor_name"] = (
        sponsor_df["sponsor_name"]
        .replace(sponsor_mapping)
    )

    sponsor_df = (
    sponsor_df
    .groupby("sponsor_name", as_index=False)
    ["number_of_trials"]
    .sum()
    .sort_values(
        "number_of_trials",
        ascending=False
    )
    .head(10)
) 

    fig = px.bar(

        sponsor_df,

        x="number_of_trials",

        y="sponsor_name",

        orientation="h"

    )


    fig.update_layout(

        margin=dict(

            l=170,

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

            color="#9CA3AF",



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