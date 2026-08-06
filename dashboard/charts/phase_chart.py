import plotly.express as px


def create_phase_chart(studies_df):

    phase_counts = (

        studies_df["phase"]
        .value_counts()
        .reset_index()

    )

    phase_counts.columns = [

        "phase",
        "number_of_studies"

    ]

    def clean_label(text):

        return (
            text
            .replace("_", " ")
            .title()
        )

    phase_counts["phase"] = (
        phase_counts["phase"]
        .apply(clean_label)
    )

    fig = px.bar(

        phase_counts,

        x="phase",

        y="number_of_studies"

    )

    fig.update_layout(

        margin=dict(

            l=60,

            r=30,

            t=20,

            b=50

        ),

        height=450,

        showlegend=False,

        xaxis_title=None,

        yaxis_title=None

    )

    fig.update_traces(

        marker_color="#142D34"

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

        )

    )

    return fig