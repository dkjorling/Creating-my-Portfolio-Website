import dash_bootstrap_components as dbc
from dash import html, register_page
from dash_bootstrap_templates import load_figure_template
from components.containers import create_project_rows, page_top, page_bottom
from components.helpers import read_text
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/portfolio')


load_figure_template('FLATLY')

### Load Text Data ###

introduction_text = read_text("data/portfolio/introduction_projects.txt")

### Configure Project Order and Get Rows ###
project_order = [
    "optionsport", "redditnlp", "wine", "fbrefapi", "soccerdb", "optdb",
    "imdb", "bettingtransformer", "nflwinner", "combine", "website"
]

# These are the project rows
project_rows = create_project_rows(project_order)

### Begin Page Layout ###

layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                html.Br(),
                # Header Row
                dbc.Row(
                    html.H2(
                        [
                        html.U(
                        "Portfolio"
                        ),
                        ],
                        style={
                            'font-size':'30px',
                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                            'font-weight':'bold',
                            'color':'#ae5000'
                        }
                    ),
                    style={
                        'margin':'0px 30px 0px 30px',
                        }
                ),
                # Introduction Row
                dbc.Row(
                    html.P(
                        introduction_text,
                        style={
                            'font-size':'16px',
                            'color':'#666600'
                        }
                    ),
                    style={
                        'margin':'0px 30px 15px 30px',
                        'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                        'background-color':'#faf0e6'
                        }
                ),
                # Project Rows
                *project_rows,

                # Empty Row for better aesthetic
                dbc.Row(
                    style={
                        'padding':'0px 0px 300px 0px'
                        }
                )
                    
                ],
            style={
                'background-color':'seashell'
            }
        ),
        page_bottom(),
    ]
)