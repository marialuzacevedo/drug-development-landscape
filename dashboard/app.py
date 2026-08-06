import pandas as pd

from sqlalchemy import create_engine

import plotly.graph_objects as go
import plotly.io as pio

from dash import Dash 

from dashboard.charts.phase_chart import create_phase_chart
from dashboard.components.layout import create_layout
from dashboard.charts.disease_chart import create_disease_chart
from dashboard.charts.sponsor_chart import create_sponsor_chart
from dashboard.charts.status_chart import create_status_chart
from dashboard.charts.location_chart import create_location_map
from dashboard.charts.enrollment_chart import create_enrollment_chart
from dashboard.charts.sponsor_type_chart import create_sponsor_type_chart


# Database


db_path = "database/drug_development_landscape.db"

engine = create_engine(
    f"sqlite:///{db_path}"
)



# Load data


studies_df = pd.read_sql(
    "SELECT * FROM studies",
    engine
)
phase_options = (
    studies_df["phase"]
    .dropna()
    .unique()
    .tolist()
)

phase_options.sort() 
phase_options.insert(0, "All")

# KPIs


total_trials = len(studies_df)

average_enrollment = studies_df["enrollment"].mean()

total_phases = studies_df["phase"].nunique()



# Plotly Theme


pio.templates["biotech"] = go.layout.Template(

    layout=dict(

        font=dict(
            family="Manrope",
            color="#142D34"
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        colorway=[
            "#142D34",
            "#337687",
            "#9CA3AF"
        ],

        xaxis=dict(
            showgrid=False,
            zeroline=False
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#EEF3F7",
            zeroline=False
        )

    )

)

pio.templates.default = "biotech"



# Charts


phase_fig = create_phase_chart(studies_df)
disease_fig = create_disease_chart(engine, studies_df)
sponsor_fig = create_sponsor_chart(engine) 
status_fig = create_status_chart(engine)
location_fig = create_location_map(engine)
enrollment_fig = create_enrollment_chart(engine)
sponsor_type_fig = create_sponsor_type_chart(engine)

# App


app = Dash(
    __name__,
    assets_folder="assets"
)


app.layout = create_layout(

    total_trials=total_trials,

    average_enrollment=average_enrollment,

    total_phases=total_phases,

    phase_fig=phase_fig,

    disease_fig=disease_fig,

    sponsor_fig=sponsor_fig,

    status_fig=status_fig,

    location_fig=location_fig,

    enrollment_fig=enrollment_fig,

    sponsor_type_fig=sponsor_type_fig,

    phase_options=phase_options 

)


if __name__ == "__main__":

    app.run(
    host="0.0.0.0",
    port=8050,
    debug=False,
    use_reloader=False
)  