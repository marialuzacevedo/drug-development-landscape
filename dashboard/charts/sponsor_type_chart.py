import pandas as pd
import plotly.express as px


def create_sponsor_type_chart(engine):

    query = """
    SELECT
        sponsor_type,
        COUNT(sponsor_id) AS number_of_sponsors
    FROM sponsors
    GROUP BY sponsor_type
    ORDER BY number_of_sponsors DESC;
    """


    sponsor_type_df = pd.read_sql(
        query,
        engine
    )

    sponsor_type_df = sponsor_type_df[
    sponsor_type_df["sponsor_type"] != "UNKNOWN"
]
    
    name_mapping = {

    "INDUSTRY": "Industry",

    "OTHER": "Other Organizations",

    "OTHER_GOV": "Government Organizations",

    "NETWORK": "Research Networks",

    "FED": "Federal Government",

    "NIH": "NIH",

    "INDIV": "Individual Investigator"

}


    sponsor_type_df["sponsor_type"] = (
        sponsor_type_df["sponsor_type"]
        .map(name_mapping)
    )

    fig = px.pie(

        sponsor_type_df,

        names="sponsor_type",

        values="number_of_sponsors",

        hole=0.65,

        color_discrete_sequence=[
        "#142D34",
        "#337687",
        "#5E98A6",
        "#7CB3BF",
        "#A8CBD3",
        "#C9E0E6"
] 

    ) 

    

    fig.update_layout(

        margin=dict(

            l=20,
            r=20,
            t=20,
            b=20

        ),

        height=450,

        showlegend=True,

        legend=dict(


            font=dict(

                family="Manrope",

                size=12,

                color="#9CA3AF"

            )

        ),
        uniformtext=dict(

            minsize=10,

            mode="hide"

        ) 


    )


    fig.update_traces(

        textinfo="percent",
        textposition="inside",
        insidetextorientation="radial",

        textfont=dict(

            family="Manrope",

            size=13

        )

    )  


    return fig