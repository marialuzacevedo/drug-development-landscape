import pandas as pd
import plotly.express as px
import numpy as np


def create_location_map(engine):

    query = """
    SELECT
        l.country,
        COUNT(sl.study_id) AS number_of_trials
    FROM study_locations sl
    JOIN locations l
        ON sl.location_id = l.location_id
    GROUP BY l.country
    ORDER BY number_of_trials DESC;
    """


    country_df = pd.read_sql(
        query,
        engine
    )
    country_df["log_trials"] = np.log1p(
    country_df["number_of_trials"]
) 

    fig = px.choropleth(

        country_df,

        locations="country",

        locationmode="country names",

        color="log_trials",

        hover_name="country",

        color_continuous_scale= [
        "#DCE8EC",
        "#337687",
        "#142D34"
    ] 

    )


    fig.update_layout(

        margin=dict(

            l=0,

            r=0,

            t=20,

            b=0

        ),

        height=550,

        coloraxis_colorbar=dict(

            title="Trials"

        )

        
    )
    fig.update_geos(

        projection_type="natural earth",

        showframe=False,

        showcountries=True

    )

    return fig