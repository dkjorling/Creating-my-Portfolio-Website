import dash_bootstrap_components as dbc
import json
import pandas as pd
import datetime as dt
import re
from dash import html, dcc, Input, Output, register_page, get_asset_url, callback, dash_table
from dash_bootstrap_templates import load_figure_template
from datetime import date
from io import BytesIO

import base64

############# my imports ##############
from dashboards.redditnlp_lakers_stats import PlayerDate
import dashboards.redditnlp_sentiment_stats as ss

####################################################################################
### load data ###

path = "assets/"
colors = ['#552583', '#FDB927', 'white', '#405ED7', "#FDB927"]

# ent dict
with open(path + 'entities_with_nicknames.json', 'r') as f:
    entities = json.load(f)
entities = dict(entities)

players = [entities[k]['init_name'] for k in list(entities.keys())[3:21]]

### define stat options ###

stat_opts = [
    'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB',
    'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS', 'OFF_RATING',
    'DEF_RATING', 'NET_RATING', 'AST_PCT', 'AST_TOV', 'AST_RATIO',
    'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'EFG_PCT', 'TS_PCT', 'USG_PCT',
    'POSS', 'PIE', 'MIN', 'FG_PCT', 'FG3_PCT', 'FT_PCT'
    ]


# initiate with lebron by default:
initial_player = players[0]
initial_date = "2023-04-10"


### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/redditnlp/dashboard/players')
load_figure_template('FLATLY')

layout = html.Div(
    children=[
        dbc.Row(
            [
            dbc.Col(
                [
                html.Div(
                    [
                    html.P(
                        "Select Player:",
                        style={
                            'color':'white',
                            'padding':'0px 0px 0px 0px',
                            'margin':'0px 10px 0px 10px',
                            'display':'inline-block'
                        }
                    ),
                    dcc.Dropdown(
                        id="player-select",
                        options=players,
                        value=initial_player,
                        clearable=False,
                        style={
                            'width':'150px',
                            'padding':'0px 0px 0px 0px',
                            'margin':'0px 0px 5px 0px',
                            'display':'inline-block',
                            'height':'25px',
                            'textAlign':'center',
                            'verticalAlign':'middle',
                            'background-color':colors[1]
                        }
                    ),
                    html.P(
                        "Select Date:",
                        style={
                            'color':'white',
                            'padding':'0px 0px 0px 0px',
                            'margin':'0px 10px 0px 10px',
                            'display':'inline-block'
                        }
                    ),
                    dcc.DatePickerSingle(
                        id="date-select",
                        date=date(2023, 4, 10),
                        min_date_allowed=date(2022, 10, 18),
                        max_date_allowed=date(2023, 4, 10),
                        initial_visible_month=date(2023, 4, 10),
                        style={
                            'margin':'0px 10px 0px 10px',
                            'padding':'0px 0px 0px 0px',
                            'display':'inline-block',
                        }
                    ),
                    

                    ],
                    
                ),
                ],
                width={'size':7}
            ),
            dbc.Col(
                [
                html.Div(
                    [
                    html.A(
                        "Team",
                        href="/redditnlp/dashboard/",
                        style={
                            'color': 'white',
                            'font-size':'20px',
                            'margin':'0px 0px 0px 0px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),

                    html.A(
                        "Documentation",
                        href="/redditnlp/dashboard/documentation",
                        style={
                            'color': 'white',
                            'font-size':'20px',
                            'margin':'0px 0px 0px 15px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),
                    html.A(
                        "Overview",
                        href="/redditnlp",
                        style={
                            'color': 'white',
                            'font-size':'20px',
                            'margin':'0px 0px 0px 15px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),

                    html.A(
                        "Portfolio",
                        href="/portfolio",
                        style={
                            'color': 'white',
                            'font-size':'20px',
                            'margin':'0px 0px 0px 15px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),
                    ]
                )
                ],
                width={'size':5},
            ),
            ],
            style={
                'background-color':'black',
                'position':'fixed',
                'width':'100%',
                'margin-botton':'5px',
                'zIndex': '999'
            }
        ),
        
        dbc.Row(
           [
            dbc.Col(
                [
                html.Img(
                    id='player-image',
                    style={
                        'height':'200px',
                        'width':'auto'
                    }
                ),

                
                ],
            ),
            dbc.Col(
                [
                html.H1(
                    id='player-name1',
                    style={
                        'color':colors[1],
                        'padding':'0px 0px 0px 0px',
                        'font-weight':'bold'
                    },
                ),
                html.H1(
                    id='player-name2',
                    style={
                        'color':colors[1],
                        'margin': '-10px 0px 0px 0px',
                        'font-weight':'bold'
                    },
                ),
                html.H2(
                    id='player-number',
                    style={
                        'color':'white',
                        'padding':'-10px 0px 0px 0px',
                        'font-weight':'bold'
                    }
                ),    
                ],
                style={
                    'textAlign':'left',
                    'padding':'30px 0px 0px 0px'
                }
            ),
            dbc.Col(
                [
                html.Div(
                    [
                    html.P(
                        "Height: ",
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 0px',
                        }
                    ),
                    html.P(
                        id='ci-1',
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),

                    ],
                    style={
                        'color':'white',
                        'padding':'0px 0px 0px 0px'
                    },
                ),
                html.Div(
                    [
                    html.P(
                        "Weight: ",
                        style={
                            'display':'inline-block',
                        }
                    ),
                    html.P(
                        id='ci-2',
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),

                    ],
                    style={
                        'color':'white',
                    },
                ),
                html.Div(
                    [
                    html.P(
                        "Position: ",
                        style={
                            'display':'inline-block',
                        }
                    ),
                    html.P(
                        id='ci-3',
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),

                    ],
                    style={
                        'color':'white',
                    },
                ),
                ],
                style={
                    'textAlign':'left',
                    'padding':'45px 0px 0px 0px'
                }
            ),
            dbc.Col(
                [
                html.Div(
                    [
                    html.P(
                        "Birthdate: ",
                        style={
                            'display':'inline-block',
                        }
                    ),
                    html.P(
                        id='ci-4',
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),

                    ],
                    style={
                        'color':'white',
                        'padding':'0px 0px 0px 0px'
                    },
                ),
                html.Div(
                    [
                    html.P(
                        "School: ",
                        style={
                            'display':'inline-block',
                        }
                    ),
                    html.P(
                        id='ci-5',
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),

                    ],
                    style={
                        'color':'white',
                    },
                ),
                html.Div(
                    [
                    html.P(
                        "Experience: ",
                        style={
                            'display':'inline-block',
                        }
                    ),
                    html.P(
                        id='ci-6',
                        style={
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),

                    ],
                    style={
                        'color':'white',
                    },
                ),
                ],
                style={
                    'textAlign':'left',
                    'padding':'45px 0px 0px 0px'
                }
            ),


            dbc.Col(
                [
                dbc.Stack(
                    [
                    html.Img(
                        src=get_asset_url('lakers1.png'),
                        style={
                            'height':'80%',
                            'width':'80%',
                            'padding-left':'40px',
                            'padding-top':'30px'
                        }
                    ),
                    
                    ]
                ),
                ],
                style={
                    'padding':'0px 0px 0px 0px',
                    'textAlign':'center',
                }
            ),

            ],
            style={
                'padding-top':'20px',
                'background-color':'black',
                'border-bottom':'3px solid  #FDB927',

            }
       ),
       dbc.Row(
           [
            dbc.Col(
                [
                html.P(
                    "Sentiment Pie Chart",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                        'font-size':'20px',
                        'padding':'20px 0px 0px 0px',
                    }
                ),
                dcc.Graph(
                    id="pie-chart",
                    #config={'displayModeBar': False},
                    style={
                        'background-color':colors[0],
                        'color':colors[0],
                        'height':'220px',
                        'margin':'0px 0px 0px 0px',
                        'padding':'0px 0px 10px 0px'
                    }
                ),
                
                ],
                width={'size':3},
                style={
                    'margin':'0px 0px 0px 30px',
                    'textAlign':'center',
                    'font-weight':'bold',
                    'border-right':'3px solid {}'.format(colors[1])
                }
            ),
            dbc.Col(
                [
                html.P(
                    "Sentiment YTD",
                    style={
                        'color':'white',
                        'font-size':'20px',
                        'font-weight':'bold'
                    }
                ),
                html.H1(
                    id="sent-ytd",
                    style={
                        'color':'white',
                        'font-weight':'bold'
                    }
                ),
                html.P(
                    "Avg. Sentiment YTD",
                    style={
                        'color':'white',
                        'font-size':'20px',
                        'font-weight':'bold'
                    }
                ),
                html.H1(
                    id="sent-ytd-avg",
                    style={
                        'color':'white',
                        'font-weight':'bold'
                    }
                ),
                ],
                width={'size':3},
                style={
                    'textAlign':'center',
                    'padding':'20px 0px 0px 0px',
                    'margin':'0px 0px 0px 0px',
                    'border-right':'3px solid {}'.format(colors[1])
                }
            ),
             dbc.Col(
                [
                html.P(
                    "20-Day Sentiment",
                    style={
                        'color':'white',
                        'font-size':'20px',
                        'font-weight':'bold'
                    }
                ),
                html.H1(
                    id="sent-recent",
                    style={
                        'color':'white',
                        'font-weight':'bold'
                        
                    }
                ),
                html.P(
                    "Avg. 20-Day Sentiment",
                    style={
                        'color':'white',
                        'font-size':'20px',
                        'font-weight':'bold'
                    }
                ),
                html.H1(
                    id="sent-recent-avg",
                    style={
                        'color':'white',
                        'font-weight':'bold'
                    }
                ),
                ],
                width={'size':3},
                style={
                    'textAlign':'center',
                    'padding':'20px 0px 0px 0px',
                    'margin':'0px 0px 0px 0px',
                    'border-right':'3px solid {}'.format(colors[1])
                }
            ),
             dbc.Col(
                [
                html.P(
                    "20-Day Trending Sentiment",
                    style={
                        'color':'white',
                        'font-size':'20px',
                        'font-weight':'bold'
                    }
                ),
                html.H1(
                    id="sent-trend",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                    }
                ),
                html.P(
                    "Avg. 20-Day Trending Sentiment",
                    style={
                        'color':'white',
                        'font-size':'20px',
                        'font-weight':'bold'
                    }
                ),
                html.H1(
                    id="sent-trend-avg",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                    }
                ),
                ],
                style={
                    'textAlign':'center',
                    'margin':'20px 0px 0px 0px'
                }
            ),

           ],
           style={
               'background-color':colors[0],
               'border-bottom':'3px solid  #FDB927',
               
           }
       ),
       dbc.Row(
           [
            dbc.Col(
                [
                html.P(
                    "Stat Type:",
                    style={
                        'color':'white',
                        'padding':'0px 0px 5px 0px',
                        'margin':'30px 0px 0px 0px',
                    }
                ),
                dcc.Dropdown(
                    id="stat-select",
                    options=[
                        {'label':'Per Game', 'value':'pg'},
                        {'label':'Per 36 Min.', 'value':'p36'},
                        {'label':'Per 100 Pos', 'value':'p100'},
                        {'label':'Cumulative', 'value':'cum'}
                    ],
                    value='pg',
                    clearable=False,
                    style={
                        'width':'200px',
                        'padding':'0px 0px 0px 0px',
                        'background-color':colors[1],
                        'color':colors[0],
                        'font-color':colors[0],
                        
                        
                    }
                ),
                html.Iframe(
                    id='yt',
                    width='95%',
                    height='80%',
                    style={
                        'padding':'15px 0px 30px 0px'
                    }
                    
                )
                ],
                width = {'size':4},
                style={
                    'margin':'0px 0px 0px 30px',
                    'font-weight':'bold',
                    'border-right':'3px solid {}'.format(colors[1]),
                }
            ),
            dbc.Col(
                [
                html.H3(
                    "Player Statistics",
                    style={
                        'margin':'30px 0px 30px 0px',
                        'font-weight':'bold',
                        'font-size':'28px',
                        'color':'white',
                        'textAlign':'center'
                    }
                ),
                html.Div(
                    id='stats-table-container',
                    className='stats-table-container',
                    children=[
                        dash_table.DataTable(
                            id='stats-table',
                            style_cell={
                                'textAlign': 'center',
                                'background-color':colors[0],
                                'color':'white',
                                'padding':'5px',
                                },
                            style_header={
                                'fontWeight': 'bold',
                                'border': '1px solid white',
                                'background-color':colors[0],
                                'font-color':colors[1],
                                'color':colors[1],
                            },
                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'background-color': colors[0],
                                    'font-color':colors[1]
                                }
                            ]
                        )
                    ],
                    style={
                        'padding':'15px 0px 30px 0px'
                    }
                ),
                html.Div(
                    id='stats-table-container2',
                    className='stats-table-container',
                    children=[
                        dash_table.DataTable(
                            id='stats-table2',
                            style_cell={
                                'textAlign': 'center',
                                'background-color':colors[0],
                                'color':'white',
                                'padding':'5px'
                                },
                            style_header={
                                'fontWeight': 'bold',
                                'border': '1px solid white',
                                'background-color':colors[0],
                                'font-color':colors[1],
                                'color':colors[1],
                            },
                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'background-color': colors[0],
                                    'font-color':colors[1]
                                }
                            ]
                        )
                    ],
                    style={
                        'padding':'15px 0px 15px 0px'
                    }
                ),
                html.Div(
                    id='stats-table-container3',
                    className='stats-table-container',
                    children=[
                        dash_table.DataTable(
                            id='stats-table3',
                            style_cell={
                                'textAlign': 'center',
                                'background-color':colors[0],
                                'color':'white',
                                'padding':'5px'
                                },
                            style_header={
                                'fontWeight': 'bold',
                                'border': '1px solid white',
                                'background-color':colors[0],
                                'font-color':colors[1],
                                'color':colors[1],
                            },
                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'background-color': colors[0],
                                    'font-color':colors[1]
                                }
                            ]
                        )
                    ],
                    style={
                        'padding':'30px 0px 0px 0px'
                    }
                ),
                ],
                style={
                    'textAlign':'center',
                }
            ),
           ],
           style={
               'padding-right':'15px',
           }
           
       ),
       dbc.Row(
           [
            html.Img(
                    id="wordcloud",
                    style={
                        'width':'100%'
                    }
                ),
           ],
       ),
       dbc.Row(
           [
            dbc.Col(
                [
                html.P(
                    "Sentiment Type:",
                    style={
                        'color':'white',
                        'padding':'0px 0px 5px 0px',
                        'margin':'15px 0px 0px 0px'
                    }
                ),
                dcc.Dropdown(
                    id="sent-select",
                    options=[
                        {'label':'All', 'value':'all'},
                        {'label':'Positive', 'value':'positive'},
                        {'label':'Negative', 'value':'negative'},
                    ],
                    value='all',
                    clearable=False,
                    style={
                        'width':'200px',
                        'padding':'0px 0px 0px 0px',
                        'background-color':colors[1],
                        'color':colors[0],
                        'font-color':colors[0]
                        
                    }
                ),
                html.P(
                    "Top Player Associations",
                    style={
                        'color': 'white',
                        'padding':'10px 0px 5px 0px',
                        'margin':'0px 0px 0px 0px'
                    }
                ),
                html.Div(
                    [
                    html.P(
                        "1.",
                        style={
                            'color': colors[1],
                            'padding':'0px 10px 5px 0px',
                            'margin':'0x 0px 0px 0px',
                            'display':'inline-block'

                        }
                    ),
                    html.P(
                        id=("rank-1"),
                        style={
                            'color': colors[1],
                            'padding':'0px 0px 5px 0px',
                            'margin':'0px 0px 0px 0px',
                            'display':'inline-block'
                        }
                    ),
                    ]
                ),
                html.Div(
                    [
                    html.P(
                        "2.",
                        style={
                            'color': colors[1],
                            'padding':'0px 10px 5px 0px',
                            'margin':'0x 0px 0px 0px',
                            'display':'inline-block'

                        }
                    ),
                    html.P(
                        id=("rank-2"),
                        style={
                            'color': colors[1],
                            'padding':'0px 0px 5px 0px',
                            'margin':'0px 0px 0px 0px',
                            'display':'inline-block'
                        }
                    ),
                    ]
                ),
                html.Div(
                    [
                    html.P(
                        "3.",
                        style={
                            'color': colors[1],
                            'padding':'0px 10px 5px 0px',
                            'margin':'0x 0px 0px 0px',
                            'display':'inline-block'

                        }
                    ),
                    html.P(
                        id=("rank-3"),
                        style={
                            'color': colors[1],
                            'padding':'0px 0px 0px 0px',
                            'margin':'0px 0px 0px 0px',
                            'display':'inline-block'
                        }
                    ),
                    ]
                ),
                ],
                width={'size':3},
                style={
                    'margin':'0px 0px 0px 30px',
                    'font-weight':'bold',
                    'border-right':'3px solid {}'.format(colors[1])
                }
                
            ),
            dbc.Col(
                [
                dcc.Graph(
                    id='top-words',
                    style={
                        'height':'280px'
                    }
                )
                ],
                width={'size':4},
                style={
                    'margin':'0px 30px 0px 0px',
                    'textAlign':'left',
                    'border-right':'3px solid {}'.format(colors[1])
                }
                
            ),
            dbc.Col(
                [
                dcc.Graph(
                    id='top-emojis',
                    style={
                        'height':'280px'
                    }
                )
                ],
                width={'size':4},
                style={
                    'margin':'10px 30px 0px 0px',
                    'textAlign':'left'
                }
                
            ),
           ],
           style={
               'border-bottom':'3px solid  #FDB927'
           }
       ),
       dbc.Row(
           [
            dcc.Graph(
                id="sentiment-1",
                style={
                    'textAlign':'center'
                }
            ),
           ],
           style={
               'background-color':colors[0],
               'width':'84%',
               'textAlign':'center',
               'margin-left':'7%',
               'margin-right':'7%',
           }
        ),
        dbc.Row(
           [
            dbc.Col(
                [
                html.P(
                    "Stat Type:",
                    style={
                        'color':'white',
                        'padding':'0px 0px 5px 0px',
                        'margin':'30px 0px 0px 0px'
                    }
                ),
                dcc.Dropdown(
                    id="stat-select2",
                    options=[
                        {'label':'Per Game', 'value':'g'},
                        {'label':'Per 36 Min.', 'value':'m'},
                        {'label':'Per 100 Pos', 'value':'p'},
                        {'label':'Team Win %', 'value':'t'}
                    ],
                    value='g',
                    clearable=False,
                    style={
                        'width':'200px',
                        'padding':'0px 0px 0px 0px',
                        'background-color':colors[1],
                        'color':colors[0],
                        'font-color':colors[0]
                        
                    }
                ),
                html.P(
                    "Select Stat:",
                    style={
                        'color':'white',
                        'padding':'0px 0px 5px 0px',
                        'margin':'30px 0px 0px 0px'
                    }
                ),
                dcc.Dropdown(
                    id="stat-select3",
                    options=stat_opts,
                    value=stat_opts[0],
                    clearable=False,
                    style={
                        'width':'200px',
                        'padding':'0px 0px 0px 0px',
                        'background-color':colors[1],
                        'color':colors[0],
                        'font-color':colors[0]
                        
                    }
                ),
                ],
                width={'size':3},
                style={
                    'margin':'0px 0px 0px 30px',
                    'font-weight':'bold',
                    'border-right':'3px solid {}'.format(colors[1])
                }
            ),
            dbc.Col(
                [
                dcc.Graph(
                    id='sentiment-2',
                    style={
                        'textAlign':'center',
                    }
                ),
                ],
                width={'size': 6},
                style={
                    'textAlign':'center',
                    'padding':'0px 30px 0px 0px',
                    'border-right':'3px solid {}'.format(colors[1])
                }
            ),
            dbc.Col(
                [
                html.H3(
                    "Correlation",
                    style={
                        'margin':'30px 0px 0px 0px',
                        'font-weight':'bold',
                        'font-size':'28px',
                        'color':'white',
                        'textAlign':'center'
                    }
                ),
                html.H5(
                    id=('sent-corr'),
                    style={
                        'padding':'70px 0px 0px 0px',
                        'font-weight':'bold',
                        'font-size':'60px',
                        'color':colors[1],
                        'textAlign':'center'
                    }
                ),
                ],
                style={
                    'textAlign':'center',
                    'padding':'0px 0px 0px 0px'
                }
            ),

           ],
           style={
               'background-color':'black'
           }
       ),

       dbc.Row(
           style={
               'background-color':'black',
               'width':'110%',
               'height':'100px'
           }
       ),

        ],
        style={
            'background-color':colors[0],
            'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
        }
                
    )


############################## callbacks #########################################

@callback(
    Output('player-image', 'src'),
    Output('player-name1', 'children'),
    Output('player-name2', 'children'),
    Output('player-number', 'children'),
    Output('ci-1', 'children'),
    Output('ci-2', 'children'),
    Output('ci-3', 'children'),
    Output('ci-4', 'children'),
    Output('ci-5', 'children'),
    Output('ci-6', 'children'),
    Output('sent-ytd', 'children'),
    Output('sent-recent', 'children'),
    Output('sent-trend', 'children'),
    Output('sent-ytd-avg', 'children'),
    Output('sent-recent-avg', 'children'),
    Output('sent-trend-avg', 'children'),
    Output('yt', 'src'),
    Output('stats-table', 'columns'),
    Output('stats-table', 'data'),
    Output('stats-table2', 'columns'),
    Output('stats-table2', 'data'),
    Output('stats-table3', 'columns'),
    Output('stats-table3', 'data'),
    Output('pie-chart', 'figure'),
    Output('wordcloud', 'src'),
    Output('rank-1', 'children'),
    Output('rank-2', 'children'),
    Output('rank-3', 'children'),
    Output('sentiment-1', 'figure'),
    Input('player-select', 'value'),
    Input('date-select', 'date'),
    Input('stat-select', 'value'),
    
    

)

def update_dashboard(player, date, stat):
    # define class object
    playerdate = PlayerDate(name=player, date=date)

    # update image
    ent_key = playerdate.ent_key
    image_path = get_asset_url("player_pics/{}.png".format(ent_key))

    # update name and number
    pname1 = playerdate.common_info.FIRST_NAME
    pname2 = playerdate.common_info.LAST_NAME
    pnumber = int(playerdate.common_info.JERSEY)

    # update common info
    height = playerdate.common_info.HEIGHT
    weight = playerdate.common_info.WEIGHT
    position = playerdate.common_info.POSITION
    birthdate = str(playerdate.common_info.BIRTHDATE)
    birthdate = re.findall(r"\b\d{4}-\d{2}-\d{2}", birthdate)[0]
    birthdate = dt.datetime.strptime(birthdate, "%Y-%m-%d")
    birthdate = dt.datetime.strftime(birthdate, "%B %d, %Y")
    school = playerdate.common_info.SCHOOL
    experience = playerdate.common_info.SEASON_EXP

    # update sent
    sent = playerdate.get_sentiment()
    # color sentiment
    if sent <= 0.1:
        col_sent='red'
    elif sent <= 0.15:
        col_sent='yellow'
    elif sent <= 0.3:
        col_sent='white'
    else:
        col_sent='green'

    # format
    sent = f'{sent:.1%}'
    sent_rec, _, diff = playerdate.get_trending_sentiment()

    # if not on team anymore, return 0% for recent/trending sentiment
    if sent_rec == 0:
        return html.Span(sent, style={'color': col_sent}), "0%", "0%"
    else:
        sent_rec = sent_rec.round(3) 
        diff = diff.round(3) 
        # color sentiment
        if sent_rec <= 0.1:
            col_rec='red'
        elif sent_rec <= 0.15:
            col_rec='yellow'
        elif sent_rec <= 0.3:
            col_rec='white'
        else:
            col_rec='green'
        # color diff
        if diff > 0:
            color_trend = 'green'
            diff = f'+{diff:.1%}'
        else:
            color_trend = 'red'
            diff = f'{diff:.1%}'
        #format sent_rec
        sent_rec = f'{sent_rec:.1%}'
    
    ### format sent ###
    sent = html.Span(sent, style={'color': col_sent})
    sent_rec = html.Span(sent_rec, style={'color': col_rec})
    diff =  html.Span(diff, style={'color': color_trend})

    # update average sent
    fn = playerdate.entities['full_name']
    sent_df = pd.read_csv("assets/all_sents/stok.csv", index_col=0, parse_dates=['datetime'])
    sent_df = sent_df[sent_df['player_ref'] != fn]
    sent2 = ss.get_sentiment(sent_df)
    # color sentiment
    
    col_sent2='white'

    # format
    sent2 = f'{sent2:.1%}'

    sent_rec2, _, diff2 = ss.get_trending_sentiment2(sent_df, date=date)

    # if not on team anymore, return 0% for recent/trending sentiment
    if sent_rec2 == 0:
        return html.Span(sent2, style={'color': col_sent}), "0%", "0%"
    else:
        sent_rec2 = sent_rec2.round(3) 
        diff2 = diff2.round(3) 
        # color sentiment
        if sent_rec2 <= 0.1:
            col_rec2='red'
        elif sent_rec2 <= 0.2:
            col_rec2='yellow'
        elif sent_rec2 <= 0.3:
            col_rec2='white'
        else:
            col_rec2='green'
        # color diff
        if diff2 > 0:
            color_trend2 = 'green'
            diff2 = f'+{diff2:.1%}'
        else:
            color_trend2 = 'red'
            diff2 = f'{diff2:.1%}'
        #format sent_rec
        sent_rec2 = f'{sent_rec2:.1%}'

    ### format sent avg ###
    sent2 = html.Span(sent2, style={'color': col_sent2})
    sent_rec2 = html.Span(sent_rec2, style={'color': col_rec2})
    diff2 = html.Span(diff2, style={'color': color_trend2})

    ## youtube highlights ##
    vid = playerdate.entities['vid_id']
    src = "https://www.youtube.com/embed/{}".format(vid)

    ### stat table 1 ###
    if stat == 'pg':
        s = playerdate.get_per_game_stats()
        suffix = "_PG"
    elif stat == 'p36':
        s = playerdate.get_per_m_minutes_stats()
        suffix = "_P36M"
    elif stat == 'p100':
        s = playerdate.get_per_p_possessions_stats()
        suffix="_P100P"
    else:
        s = playerdate.get_cum_stats()
        suffix = ""

    cols_og = [
        'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO', 'MIN',
        'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'PF'
        ]
    
    cols = [x + suffix for x in cols_og]
    s = s.to_frame().T #keep 13-14
    s = s[
        cols
    ]
    s.columns=[x.lower().capitalize() for x in cols_og]
    cols1 = [{'name': col, 'id': col} for col in s.columns]
    data_dict1 = s.to_dict('records')

    ### stat table 2 ###
    s2 = playerdate.get_per_game_stats()
    s2 = s2.to_frame().T 
    
    cols_og2 = [
        'NET_RATING', 'OFF_RATING', 'DEF_RATING',
        'REB_PCT', 'AST_PCT', 'USG_PCT', 'PACE', 'PIE'
    ]

    s2 = s2[
        cols_og2
    ]

    s2.columns = [
        'NRtg', 'ORtg', 'DRtg', 'RebPct',
        'AstPct', 'UsgPct', 'Pace', 'PIE'
    ]

    cols2 = [{'name': col, 'id': col} for col in s2.columns]
    data_dict2 = s2.to_dict('records')

    ### stat table 3 ###
    s3 = playerdate.get_per_game_stats()
    s3 = s3.to_frame().T 

    cols_og3 = [
        'TS_PCT','EFG_PCT', 'GAMES', 'FG_PCT', 'FG3_PCT', 'FT_PCT',
        'AST_TOV', 'AST_RATIO'

    ]

    s3 = s3[
        cols_og3
    ]

    s3.columns = [
        'TsPct', 'EfgPct', 'Games', 'FgPct', 'Fg3Pct', 'FtPct',
        'AstTov', 'AstRat'

    ]

    cols3 = [{'name': col, 'id': col} for col in s3.columns]
    data_dict3 = s3.to_dict('records')

    # pie chart
    fig = playerdate.basic_pie_chart()
    fig.update_layout(
        plot_bgcolor=colors[0],
        paper_bgcolor=colors[0],
    )

    #wordcloud
    wordcloud = playerdate.generate_wordcloud()
    img = BytesIO()
    wordcloud.save(img, format='PNG')
    wc = 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

    # top assoc
    p_list = playerdate.get_top_players()
    fn = list(p_list.index[:3])

    r1 = [entities[x]['init_name'] for x in entities.keys() if entities[x]['full_name'] == fn[0]][0]
    r2 = [entities[x]['init_name'] for x in entities.keys() if entities[x]['full_name'] == fn[1]][0]
    r3 = [entities[x]['init_name'] for x in entities.keys() if entities[x]['full_name'] == fn[2]][0]

    # update sentiment 1
    sent_fig1 = playerdate.plot_sentiment_through_time()
    

    return (
        image_path, pname1, pname2,
        pnumber, height, weight,
        position, birthdate, school,
        experience, sent, sent_rec,
        diff, sent2, sent_rec2, diff2,
        src, cols1, data_dict1,
        cols2, data_dict2, cols3,
        data_dict3, fig, wc,
        r1, r2, r3,
        sent_fig1
    )

@callback(
    Output('top-words', 'figure'),
    Output('top-emojis', 'figure'),
    Input('player-select', 'value'),
    Input('date-select', 'date'),
    Input('sent-select', 'value'),
)

def update_top(player, date, sentiment):
    playerdate = PlayerDate(name=player, date=date)
    top_words = playerdate.plot_top_ten(kind=sentiment)
    top_emojis = playerdate.plot_top_ten_emoji(kind=sentiment)

    return top_words, top_emojis


@callback(
    Output('sentiment-2', 'figure'),
    Output('sent-corr', 'children'),
    Input('player-select', 'value'),
    Input('date-select', 'date'),
    Input('stat-select2', 'value'),
    Input('stat-select3', 'value')
) 

def update_corr(player, date, stat2, stat3):
    playerdate = PlayerDate(name=player, date=date)
    sent_fig2 = playerdate.sent_vs_stat(stat_col=stat3, kind=stat2)
    corr = playerdate.sent_vs_stat_corr(stat3, kind=stat2)

    if corr < 0:
        col_corr='red'
    else:
        col_corr='green'

    corr = f'{corr:.3}'
    corr = html.Span(corr, style={'color': col_corr})

    return sent_fig2, corr




