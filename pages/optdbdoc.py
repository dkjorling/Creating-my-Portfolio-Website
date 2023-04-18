import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, callback
from dash_bootstrap_templates import load_figure_template

# my imports
from dash_helpers import dashboard_navbar2, page_bottom

# create vapor color theme dictionary
colors = {
    'bg':'#1a0933',
    'purple':'#6f42c1',
    'font':'#32fbe2',
    'pink':'#ea39b8',
    'green':'#3cf281'
}
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/optdb/dashboard/documentation', theme=dbc.themes.VAPOR)


load_figure_template('VAPOR')

layout = html.Div(
            children=[
                dashboard_navbar2(
                        'optdb',
                        colors['purple'],
                        'white',
                        colors['purple']
                ),
                dbc.Row(
                    [
                    html.H3(
                        'Real-Time Option Implied Volatility Surface Documentation',
                        style={
                        'color':'#3cf281',
                        }
                    )
                    ],
                    style={
                        'font-color':'#32fbe2',
                        'background-color':'#1a0933',
                        'margin':'0px 0px 0px 0px',
                        'border-left':'20px solid #6f42c1',
                        'border-right':'20px solid #6f42c1',
                        'border-bottom':'5px solid #6f42c1',
                    }
                ),
                dbc.Row(
                    [
                    html.H5(
                        'Using the Surface Plot',
                        style={
                        'color':'#3cf281',
                        'font-size':'18px'
                        }
                    ),
                    html.P(
                        "The Surface plot panel pulls real-time Yahoo Finance implied volatility data for any stock that has listed options data and returns a 3D implied volatility surface. To use the dashboard, users can type in a stock name of their choice, and allow a few seconds to load. Clicking the plot allows users to rotate the 3D surface while hovering over the surface displays the strike-expiration-implied volatility coordinates.",
                        style={
                            'color':'white',
                            'background-color':'#1a0933',
                            'margin':'0px 0px 0px 0px',

                        }
                    ),
                    ],
                    style={
                        'font-color':'#32fbe2',
                        'margin':'0px 0px 0px 0px',
                        'border-left':'20px solid #6f42c1',
                        'border-right':'20px solid #6f42c1',
                        'border-top':'5px solid #6f42c1',
                        'border-bottom':'5px solid #6f42c1',
                        'padding':'5px 0px 5px 0px'

                    }
                ),
                dbc.Row(
                    [
                    html.H5(
                        'Using the Strike/Expiration Plots',
                        style={
                        'color':'#3cf281',
                        'font-size':'18px'
                        }
                    ),
                    html.P(
                        "The Strike and Expiration Implied Volatility Plots allow users to view 2D plots of implied volatility over all strikes given and expiration, or over all expirations given a strike price. Hovering over any point displays its coordinates, similar to the surface plot. Users must input valid listed expiration dates and strike prices for the plots to initialize. ",
                        style={
                            'color':'white',
                            'margin':'0px 0px 0px 0px',

                        }
                    ),

                    ],
                    style={
                        'font-color':'#32fbe2',
                        'background-color':'#1a0933',
                        'margin':'0px 0px 0px 0px',
                        'border-left':'20px solid #6f42c1',
                        'border-right':'20px solid #6f42c1',
                        'border-top':'5px solid #6f42c1',
                        'border-bottom':'20px solid #6f42c1',
                        'padding':'5px 0px 5px 0px'

                    }
                ),

                dbc.Row(
                    style={
                        'background-color':'#1a0933',
                        'height':'300px',   
                    }
                ),

                dbc.Row(
                    style={
                        'background-color':'#6f42c1',
                        'height':'300px',   

                    }
                ),
                page_bottom(col1='#1a0933', col2='#6f42c1', col3='white')
            ],
            style={
                'background-color':'#1a0933',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        )   
