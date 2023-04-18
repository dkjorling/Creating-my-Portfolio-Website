import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/redditnlp')


load_figure_template('FLATLY')

### Begin Page Layout ###
layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            "Entity-Level Sentiment Analysis with Reddit Data",
                            style={
                                'font-size':'30px',
                                'color':'#ae5000',
                                'font-weight':'bold'
                            }
                        ),
                        style={
                            'margin':'30px 30px 0px 30px',

                        }
                    ),
                    ]
                ),
                html.Div(
                    children=[
                        html.A(
                            html.Button(
                                    "Dashboard",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/redditnlp/dashboard',
                            style={
                                'padding':'0px 15px 0px 30px',
                                'textAlign':'center'
                            }
                        ),
                        html.A(
                            html.Button(
                                    "Code",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/redditnlp',
                            style={
                                'padding':'15px 0px 15px 0px',
                                'textAlign':'center'
                            }
                        ),
                    ],
                    style={
                        'padding':'15px 0px 15px 0px',
                        'textAlign':'left'
                    }
                ),
                                
                dbc.Row(
                    [
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
                    ]
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.P(
                            "I am currently working on a project that aims to track sentiment analysis for individual players on the Los Angeles Lakers team over the course of the 2022-23 season. To accomplish this, I utilized the reddit API to gather all post and comment data from the Lakers subreddit starting from the beginning of the season until the final play-in game before the playoffs.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "To identify individual players on the team, I will be using the spaCy library for entity recognition. After isolating player names, I will use the vaderSentiment library to determine the trending sentiment for each player at different periods in time.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "My ultimate goal is to develop an application that allows users to compare sentiment trends of different players over time. To enhance the user experience, I will also incorporate player statistics so that users can compare a player’s trending statistical performance with their trending sentiment.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        ],
                        style={
                            'margin':'0px 30px 15px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
    
                    ]
                ),
                dbc.Row(
                    [
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
                ]
                ),
                
                html.Ul(
                    [
                    html.Li(
                        html.Div(
                            [
                            html.Span(
                                "Web Scraping with requests",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "",
                            ],
                            style={
                                'color':'#ae5000',
                                'font-size':'16px',
                                'textAlign':'left',
                                'padding':'5px',
                                
                            }
                        ),
                    ),
                    html.Li(
                        html.Div(
                            [
                            html.Span(
                                "Entity recognition with spaCy",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "",
                            ],
                            style={
                                'color':'#ae5000',
                                'font-size':'16px',
                                'textAlign':'left',
                                'padding':'5px',
                                
                            }
                        ),
                    ),
                    html.Li(
                        html.Div(
                            [
                            html.Span(
                                "Sentiment analysis with vaderSentiment:",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "",
                            ],
                            style={
                                'color':'#ae5000',
                                'font-size':'16px',
                                'textAlign':'left',
                                'padding':'5px',
                                
                            }
                        ),
                    ),
                    html.Li(
                        html.Div(
                            [
                            html.Span(
                                "Libraries/Modules: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "requests, spaCy, vaderSentiment, nltk, pandas, Dash",
                            ],
                            style={
                                'color':'#666600',
                                'font-size':'16px',
                                'textAlign':'left',
                                'padding':'5px',
                                
                            }
                        ),
                    ),
                    ],
                    style={
                        'list-style-position':'outside',
                        'list-style-type':'square',
                        'background-color':'#faf0e6',
                        'margin':'0px 15px 0px 15px'
                    }
                ),
                dbc.Row(
                    style={
                        'background-color':'seashell',
                        'height':'300px',   
                        'width':'110%'
                    }
                ),
            ],
            style={
                'background-color':'seashell',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        ),
        page_bottom(),
    ]
)


