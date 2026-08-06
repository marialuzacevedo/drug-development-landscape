import pandas as pd
import plotly.express as px


def create_disease_chart(engine, filtered_df):

    study_ids= tuple(
        filtered_df["study_id"].tolist() 
    ) 
    
    query = f"""
    SELECT
        c.condition,
        COUNT(sc.study_id) AS number_of_trials
    FROM study_conditions sc
    JOIN conditions c
        ON sc.condition_id = c.condition_id
    WHERE sc.study_id IN {study_ids}

    AND c.condition NOT IN (
        'Healthy',
        'Healthy Volunteers'
    )
    GROUP BY c.condition
    ORDER BY number_of_trials DESC
    LIMIT 10;
    """

    disease_df = pd.read_sql(
        query,
        engine
    )


    fig = px.bar(

        disease_df,

        x="number_of_trials",

        y="condition",

        orientation="h"

    )


    fig.update_layout(

        margin=dict(

            l=130,

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

        marker_color="#5E98A6"

    )


    fig.update_yaxes(

        categoryorder="total ascending",

        tickfont=dict(

            family="Manrope",

            size=11,

            color="#9CA3AF",



        ),
        showgrid=False,
        zeroline=False

    )


    fig.update_xaxes(

        tickfont=dict(

            family="Manrope",

            size=12,

            color="#9CA3AF"

        )

    )


    return fig