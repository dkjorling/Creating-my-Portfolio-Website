import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom

####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/cv')


load_figure_template('FLATLY')

layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            "Dylan C.V.",
                            style={
                                'font-size':'30px',
                                'color':'black',
                                'font-weight':'bold',
                                'font-color':'black'
                            }
                        ),
                        style={
                            'margin':'30px 30px 0px 30px',

                        }
                    ),
                    ],
                ),
                html.Div(
                    [
                    dbc.Row(
                        html.H3(
                            "Core Competencies/Areas of Expertise",
                            style={
                                'color':'black'
                            }
                        )
                    )
                ]
                    
                ),
            ],
        ), 
        page_bottom(),
    ],
)
            