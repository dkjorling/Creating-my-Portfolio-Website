import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom


####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/')


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
                            '',
                            style={

                            }
                        ),
                        style={

                            'textAlign':'center'
                        }
                    ),
                    ],
                    style={
                        'height':'0px',
                        'width':'100%'
                        }
                ),
                dbc.Row([
                    dbc.Col(
                        html.H2([
                            'Transforming',
                            html.Br(),
                            'Data',
                            html.Br(),
                            'Into',
                            html.Br(),
                            'Knowledge.'
                            ],
                            style={
                                'color': 'white',
                                'padding':'90px 0px 0px 250px',
                                'font-size':'45px',
                                'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                'font-weight':'bold'
                            }
                        ),
                        style={

                            'textAlign':'left'
                        }
                    ),
                    ],
                    style={
                        'background-image':'url("assets/sun5.png")',
                        'bacgkround-repeat':'no-repeat',
                        'background-size': 'cover',
                        'background-position': 'left bottom',
                        'max-width':'120%',
                        'max-height':'110%',
                        'height':'450px',
                        'border-bottom': '3px solid #ae5000'
                        }
                ),
                
                dbc.Row([
                    dbc.Col([
                        html.H2(
                            "WELCOME.",
                            style={
                                'color': '#ae5000',
                                'font-size':'50px',
                                'padding':'30px 0px 5px 60px',
                                'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                'font-weight':'bold'
                                
                            }
                        ),
                        html.H2(
                            "Click \"Portfolio\" to view my Projects and Dashboards.",
                            style={
                                'color': '#666600',
                                'font-size':'30px',
                                'padding':'5px 0px 200px 60px',
                                'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                }
                            )
                        ],
                        style={
                            'textAlign':'left'
                        }
                    ),
                    ],
                    style={
                        'height':'300px',
                        'width':'100%',
                        'background-color':'seashell',
                    }
                ),
                dbc.Row(
                    style={
                        'padding':'0px 0px 200px 0px'
                        }
                )
            ],
            style={
                'background-color':'seashell',
                'width':'100%'
                
                  }
        ),
        page_bottom()
    ]
)
    
   
