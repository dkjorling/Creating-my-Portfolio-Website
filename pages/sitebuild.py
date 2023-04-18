import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/sitebuild')


load_figure_template('FLATLY')

### Begin Page Layout ###
layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                dbc.Row([
                    dbc.Col(
                        html.H2(
                            "Creating this Website",
                            style={
                                'font-size':'30px',
                                'color':'#ae5000'
                            }
                        ),
                        style={
                            'margin':'30px 30px 0px 30px',

                        }
                    ),
                ]),
                
                dbc.Row([
                    dbc.Col(
                        html.H2(
                            "Overview",
                            style={
                                'font-size':'22px',
                                'color':'#666600'
                            }
                        ),
                        style={
                            'margin':'0px 30px 0px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
                ]),
                
                
                dbc.Row([
                    dbc.Col(
                        html.P(
                            "",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        style={
                            'margin':'0px 30px 15px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
    
                ]),
                
                dbc.Row([
                    dbc.Col(
                        html.H2(
                            "Skill Highlights",
                            style={
                                'font-size':'22px',
                                'color':'#666600'
                            }
                        ),
                        style={
                            'margin':'15px 30px 0px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
                ]),
                
                dbc.Row([
                    dbc.Col(
                        html.P(
                            "",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        style={
                            'margin':'0px 30px 15px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
    
                ]),
                
                html.Div(
                    children=[
                        
                        html.A(
                            html.Button(
                                    "Code",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/sitebuild',
                            style={
                                'padding':'0px 0px 0px 0px',
                                'textAlign':'center'
                            }
                        ),
                        
                    ],
                    style={
                        'padding':'15px 0px 15px 0px',
                        'textAlign':'center'
                         }
                ),
            ],
            style={
                'background-color':'seashell'
            }
        ),
        page_bottom(),
    ]
)


