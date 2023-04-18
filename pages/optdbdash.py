import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, callback
from dash_bootstrap_templates import load_figure_template
from dash.dependencies import Input, Output

# import local .py files
import Visualizationyf as vs
import Tickers as tick
from dash_helpers import dashboard_navbar, page_bottom


####################################################################################

# create vapor color theme dictionary
colors = {
    'bg':'#1a0933',
    'purple':'#6f42c1',
    'font':'#32fbe2',
    'pink':'#ea39b8',
    'green':'#3cf281'
}
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/optdb/dashboard', theme=dbc.themes.VAPOR)


load_figure_template('VAPOR')

### Begin Page Layout ###
layout = html.Div(
            children=[
                dashboard_navbar(
                        'optdb',
                        colors['purple'],
                        'white',
                        colors['purple']
                ),
                dbc.Row(
                    [
                    html.H3(
                        'Real-Time Option Implied Volatility Surface',
                        style={
                        'color':'#44d9e8',
                        'font-weight':'bold'
                        }
                    )
                    ],
                    style={
                        'font-color':'#32fbe2',
                        'background-color':'#1a0933',
                        'margin':'0px 0px 0px 0px',
                        'width':'100%',
                        'border-left':'20px solid #6f42c1',
                        'border-right':'20px solid #6f42c1',
                        'text-decoration':'underline',
                        'text-decoration-color':'#44d9e8',
                        'font-weight':'bold'
                    }
                ),
                html.Div(
                    children=[
                        html.P(
                            "Ticker:",
                            style={
                                'color':'#44d9e8',
                                'display':'inline-block',
                                'font-size':'20px'
                            }
                        ),
                        dcc.Input(
                            id="sel_asset1",
                            type="text",
                            placeholder="Ticker",
                            value='SPY',
                            style={
                                'background-color': '#44d9e8',
                                'color': colors['purple'],
                                'textAlign':'center',
                                'width':'70px',
                                'display':'inline-block',
                                'margin':'0px 15px 10px 15px'
                            }
                        ),
                        html.Div(
                            id='asset_price',
                            style={
                                'color':'#44d9e8',
                                'font-color':'#44d9e8',
                                'display':'inline-block',
                                'font-size':'20px'
                            }
                        )

                        ],
                        style={
                            'display':'flex',
                            'padding':'0px 0px 0px 15px',
                            'width':'100%',
                            'border-left':'20px solid #6f42c1',
                            'border-right':'20px solid #6f42c1'
                        }
                    ),

                dbc.Row(
                    [
                    dcc.Graph(
                        id='vol_surface',
                        style={
                            'height':'100%',
                        }
                        
                    )
                    ],
                    style={
                        'background-color':'#1a0933',
                        'width':'100%',
                        'border-bottom':'20px solid #6f42c1',
                        'border-top':'20px solid #6f42c1',
                        'border-left':'20px solid #6f42c1',
                        'border-right':'20px solid #6f42c1',
                        'margin':'0px'
                        
                    }
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.Div(
                            children=[
                                html.P(
                                    "Expiration:",
                                    style={
                                        'color':'#44d9e8',
                                        'display':'inline-block',
                                        'font-size':'20px'
                                    }
                                ),
                                dcc.Input(
                                    id="sel_exp",
                                    type="text",
                                    placeholder="Ticker",
                                    value='12-15-23',
                                    style={
                                        'background-color': '#44d9e8',
                                        'color': colors['purple'],
                                        'textAlign':'center',
                                        'width':'90px',
                                        'display':'inline-block',
                                        'margin':'0px 0px 10px 15px'
                                    }
                                ),

                                ],
                                style={
                                    'display':'flex',
                                    'padding':'0px 0px 0px 45px',
                                    'width':'100%'
                                }
                        ),
                        ],
                        style={
                            'border-right':'10px solid #6f42c1',
                            'padding':'5px 0px 0px 0px'
                        }
                    ),
                    dbc.Col(
                        [
                        html.Div(
                            children=[
                                html.P(
                                    "Strike:",
                                    style={
                                        'color':'#44d9e8',
                                        'display':'inline-block',
                                        'font-size':'20px'
                                    }
                                ),
                                dcc.Input(
                                    id="sel_strike",
                                    type="number",
                                    placeholder="Strike",
                                    value=410,
                                    style={
                                        'background-color': '#44d9e8',
                                        'color': colors['purple'],
                                        'textAlign':'center',
                                        'width':'70px',
                                        'display':'inline-block',
                                        'margin':'0px 0px 10px 15px'
                                    }
                                ),

                                ],
                                style={
                                    'display':'flex',
                                    'padding':'0px 0px 0px 45px',
                                    'width':'100%'
                                }
                        ),
                        ],
                        style={
                            'padding':'5px 0px 0px 0px',
                            'border-left':'10px solid #6f42c1'
                        }
                    ),
                    ],
                    style={
                        'border-right':'30px solid #6f42c1',
                        'border-left':'30px solid #6f42c1'
                    }
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        dcc.Graph(
                            id='vol_exp'
                        )
                        ],
                        style={
                            'border-right':'10px solid #6f42c1',
                        }
                    ),
                    dbc.Col(
                        [
                        dcc.Graph(
                            id='vol_strike'
                        )
                        ],
                        style={
                            'border-left':'10px solid #6f42c1',
                        }
                    ),
                    ],
                    style={
                        'background-color':'#1a0933',
                        'width':'100%',
                        'border-bottom':'20px solid #6f42c1',
                        'border-top':'20px solid #6f42c1',
                        'border-left':'20px solid #6f42c1',
                        'border-right':'20px solid #6f42c1',
                        'margin':'0px'
                    }
                ),
                dbc.Row(
                    style={
                        'background-color':'#6f42c1',
                        'height':'300px',   
                        'width':'110%'
                    }
                ),
                page_bottom(col1='#1a0933', col2='#1a0933', col3='white')
            ],
            style={
                'background-color':'#1a0933',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        )
                
    
@callback(
    Output('vol_surface', 'figure'),
    Input('sel_asset1', 'value')
)

def update_fig_1(asset):
    fig = vs.plot_surface(asset)
    
    return fig

@callback(
    Output('asset_price', 'children'),
    Input('sel_asset1', 'value')
)

def update_price(asset):
    price = tick.get_price(asset)
    return "Current Underlying Price: {}".format(price)

@callback(
    Output('vol_exp', 'figure'),
    Input('sel_asset1', 'value'),
    Input('sel_exp', 'value')
)

def update_fig_2(asset, exp):
    fig = vs.plot_exp(asset, exp)
    
    return fig

@callback(
    Output('vol_strike', 'figure'),
    Input('sel_asset1', 'value'),
    Input('sel_strike', 'value')
)

def update_fig_3(asset, strike):
    fig = vs.plot_strike(asset, strike)
    
    return fig

