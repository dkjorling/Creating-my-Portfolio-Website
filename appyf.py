import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import yfinance as yf
import sys
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output, page_container, page_registry, callback
from datetime import datetime as dt
from datetime import date
from plotly.subplots import make_subplots
from dash_bootstrap_templates import load_figure_template
from dash.dependencies import Input, Output

# import local .py files
import Tickers as tick
import Visualization as vs

################################################################################################################################
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/")),
                dbc.NavItem(dbc.NavLink("Data Visuals", href="/analysis")),
                dbc.NavItem(dbc.NavLink("Documentation", href="/documentation")),
                dbc.NavItem(dbc.NavLink("About", href="/about"))
                
            ] ,
            color="light",
            light=True,
        ), 
    ])

    return layout

app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])

load_figure_template('Vapor')

app.layout = html.Div(children=[
    dbc.Row([html.H1('Real-time Option Volatility Surface Visualization')
            ]),
    dbc.Row([
            dbc.Stack([
                html.P("Select Asset:"),
                dcc.Input(
                    id="sel_asset",
                    type="test",
                    placeholder="Type Asset"),
            ])
    ]),
    dbc.Row([
            dcc.Graph(id='vol_surface')
    ])
])
                
    
@callback(
    Output('vol_surface', 'figure'),
    Input('sel_asset', 'value')

)

def update_fig_1(asset):
    fig = vs.plot_surface(asset)
    
    return fig


if __name__ == '__main__':
    app.run(debug=False)