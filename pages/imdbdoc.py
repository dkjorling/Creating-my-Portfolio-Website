import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page

from dash_bootstrap_templates import load_figure_template

# my imports
from dash_helpers import dashboard_navbar2, page_bottom

### Save Style ###
doc_style = {'padding':'0px 15px'}

####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/imdb/dashboard/documentation')

load_figure_template('FLATLY')

### Begin Page Layout ###
layout = html.Div(
            children=[
                dashboard_navbar2(
                        'imdb',
                        '#e8b20c',
                        'black',
                        '#e8b20c'
                ),
                dbc.Row(
                    [
                    html.H3(
                        'Box Office Profit Predictor Usage Notes',
                        style={
                        'color':'#e8b20c',
                        'font-weight':'bold'
                        }
                    ),
                    html.P(
                        "This dashboard is connected to a trained fully-connected neural network which takes in various input features and outputs estimated box office profits. Users can choose from millions of combinations, including thousands of actors, actresses and directors. The actors and actresses are modeled by a feature-engineered variable called 'star power', which is a numerical predictor based on the amount of times each actor/actress appears as a 'star' in the dataset. This was used as a proxy for actor popularity and ended up being one of strongest predictors for box office profits. Similarly, each director in the dataset is given a 'director popularity' score which is also used as a numerical predictor in the model. ",
                        style={
                            'color':'silver'
                        }
                    ),
                    html.Br(),
                    html.P(
                        "Note that the dataset spans a timeframe of 1990-2019 as the purpose of this project was to determine profit drivers in modern film. Data after 2019 was not used due to the global pandemic which heavily skewed profits downward, although the industry is now showing signs of steady recovery. Finally, each obervation used in the study was inflation-adjusted to 2022 dollars and therefore any resulting dashboard outputs should be thought of in terms of 2022 dollars.",
                        style={
                            'color':'silver'
                        }
                    )
                    ],
                    style={
                        'padding':'15px 60px 15px 30px'
                    }
                ),
                html.Div(
                    style={
                        'height':'300px',
                    }
                ),
                html.Div(
                    style={
                        'height':'300px',
                        'background-color':'silver'
                    }
                ),
                page_bottom(col1='silver', col2='silver', col3='black')
            ],
            style={
                'background-color':'black',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        )   
                
                      

        
        
        
        
        
        
        
        
        
        
    

