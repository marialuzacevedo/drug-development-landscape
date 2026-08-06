from dash import html, dcc

from dashboard.components.kpi import kpi_card


def create_layout(

    total_trials,

    average_enrollment,

    total_phases,

    phase_fig,

    disease_fig,

    sponsor_fig,

    status_fig,

    location_fig,

    enrollment_fig,

    sponsor_type_fig,

    phase_options

):

    return html.Div( 

[ 
            # Header
            
            html.Div(

                [

                    html.H1(

                        "Clinical Trial Intelligence Dashboard",

                        className="dashboard-title"

                    ),

                    html.P(

                        "Exploring sponsors, diseases, recruitment status, clinical phases and global trial locations.",

                        className="dashboard-subtitle"

                    )

                ],

                className="header"

            ),
            
            # KPI Section
            

            html.Div(

                [

                    kpi_card(f"{total_trials:,}", "Total Trials"),

                    kpi_card(f"{round(average_enrollment):,}", "Average Enrollment"),

                    kpi_card(total_phases, "Clinical Phases")

                ],

                className="kpi-container"

            ),



# Row 1


html.Div(

    [

        html.Div(

            [

                html.H3(

                    "Clinical Trials by Phase",

                    className="graph-title"

                ),

                dcc.Graph(

                    id="phase-chart", 
                    
                    figure=phase_fig, 

                    config={"displayModeBar": False}

                )

            ],

            className="graph-card"

        ),


        html.Div(

            [

                html.H3(

                    "Recruitment Status",

                    className="graph-title"

                ),

                dcc.Graph(

                    figure=status_fig,

                    config={"displayModeBar": False}

                )

            ],

            className="graph-card"

        )

    ],

    className="graph-row"

),

            
            # Row 2
            

            html.Div(

                [

                    html.Div(

                        [

                            html.H3(

                                "Most Studied Therapeutic Areas",

                                className="graph-title"

                            ),

                            dcc.Graph(

                                id="disease-chart",  
                                figure=disease_fig,
                                config={"displayModeBar": False}

                            ) 

                        ],

                        className="graph-card"

                    ),


                    html.Div(

                        [

                            html.H3(

                                "Average Enrollment by Phase",

                                className="graph-title"

                            ),

                            dcc.Graph(

                                figure=enrollment_fig,
                                config={"displayModeBar": False}

                            )

                        ],

                        className="graph-card"

                    )

                ],

                className="graph-row"

            ),

            # Row 3
            

            html.Div(

                [

                    html.Div(

                        [

                            html.H3(

                                "Leading Clinical Trial Sponsors", 

                                className="graph-title"

                            ),

                            dcc.Graph(

                                figure=sponsor_fig,
                                config={"displayModeBar": False}

                            )

                        ],

                        className="graph-card"

                    ),


                    html.Div(

                        [

                            html.H3(

                                "Sponsor Type Distribution",

                                className="graph-title"

                            ),

                            dcc.Graph(

                                figure=sponsor_type_fig,
                                config={"displayModeBar": False}

                            )

                        ],

                        className="graph-card"

                    )

                ],

                className="graph-row"

            ), 

            # Map
            

    html.Div(

                [
 
                    html.H3(

                        "Clinical Trial Locations",

                        className="graph-title"

                    ),

                    dcc.Graph(

                        figure=location_fig,
                        config={"displayModeBar": False}

                    )

                ],

                className="graph-card single-graph"

            ),  
    
    # Footer

    html.Div(

        [

            html.P(

                "Data source: ClinicalTrials.gov API | Last updated: August 2026",

                className="footer-text"

            )

        ],

        className="dashboard-footer"

    )   

],
className="dashboard"   
    )  

