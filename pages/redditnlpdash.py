import dash_bootstrap_components as dbc
import json
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url, callback, dash_table
from dash_bootstrap_templates import load_figure_template
from datetime import date
from io import BytesIO
import re
import base64

############# my imports ##############
import lakers_stats as ls
from lakers_stats import TeamDate
import Visualizationred as vs
import sentiment_stats as ss

####################################################################################
### load data ###

path = "assets/"
colors = ['#552583', '#FDB927', 'white', '#405ED7', "#FDB927"]

# ent dict
with open(path + 'entities_with_nicknames.json', 'r') as f:
    entities = json.load(f)
entities = dict(entities)

fo = [entities[k]['init_name'] for k in list(entities.keys())[:3]]

### define stat options ###

stat_opts = [
    'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB',
    'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS', 'OFF_RATING',
    'DEF_RATING', 'NET_RATING', 'AST_PCT', 'AST_TOV', 'AST_RATIO',
    'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'EFG_PCT', 'TS_PCT', 'USG_PCT',
    'POSS', 'PIE', 'MIN', 'FG_PCT', 'FG3_PCT', 'FT_PCT'
    ]

###################################################################################


####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/redditnlp/dashboard/')
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
                        "Select Entity:",
                        style={
                            'color':'white',
                            'padding':'0px 0px 0px 0px',
                            'margin':'0px 10px 0px 10px',
                            'display':'inline-block'
                        }
                    ),
                    dcc.Dropdown(
                        id="entity-select",
                        options=[
                            {'label':'Team', 'value':'team'},
                            {'label':'Jeanie Buss', 'value':'jeanie_buss'},
                            {'label':'Rob Pelinka', 'value':'rob_pelinka'},
                            {'label':'Darvin Ham', 'value':'darvin_ham'},
                        ],
                        value='team',
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
                        id="date-select-team",
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
                        "Players",
                        href="/redditnlp/dashboard/players",
                        style={
                            'color': 'white',
                            'font-size':'20px',
                            'margin':'0px 0px 0px 0px',
                            'font-weight':'bold'
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
                width={'size':5}
            )
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
                    src=get_asset_url("lakers1.png"),
                    style={
                        'height':'80%',
                        'width':'auto'
                    }
                ),
                ],
                style={
                    'padding':'30px 0px 0px 0px'
                }
            ),
            dbc.Col(
                [
                html.H1(
                    "Los Angeles",
                    style={
                        'color':colors[1],
                        'padding':'0px 0px 0px 0px',
                        'font-weight':'bold'
                    },
                ),
                html.H1(
                    "Lakers",
                    style={
                        'color':'white',
                        'margin': '-10px 0px 0px 0px',
                        'font-weight':'bold'
                    },
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
                    html.H4(
                    "Record:",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                        'display':'inline-block',
                    }
                    ),
                    html.H4(
                        id=('record'),
                        style={
                            'color':colors[1],
                            'font-weight':'bold',
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),
                    ]
                ),
                html.Div(
                    [
                    html.H4(
                    "WC Rank:",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                        'display':'inline-block',
                    }
                    ),
                    html.H4(
                        id=('rank'),
                        style={
                            'color':colors[1],
                            'font-weight':'bold',
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),
                    ]
                ),
                html.Div(
                    [
                    html.H4(
                    "Last 10:",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                        'display':'inline-block',
                    }
                    ),
                    html.H4(
                        id=('last-ten'),
                        style={
                            'color':colors[1],
                            'font-weight':'bold',
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),
                    ]
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
                    html.H4(
                    "Streak:",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                        'display':'inline-block',
                    }
                    ),
                    html.H4(
                        id=('streak'),
                        style={
                            'color':colors[1],
                            'font-weight':'bold',
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),
                    ]
                ),
                html.Div(
                    [
                    html.H4(
                    "Win Pct:",
                    style={
                        'color':'white',
                        'font-weight':'bold',
                        'display':'inline-block',
                    }
                    ),
                    html.H4(
                        id=('win-pct'),
                        style={
                            'color':colors[1],
                            'font-weight':'bold',
                            'display':'inline-block',
                            'padding':'0px 0px 0px 5px'
                        }
                    ),
                    ]
                ),
                ],
                style={
                    'textAlign':'left',
                    'padding':'45px 0px 0px 0px'
                }
            )
            
           ],
           style={
                'background-color':'black'
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
                    id="pie-chart-team",
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
                    id="sent-ytd-team",
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
                    id="sent-recent-team",
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
                    id="sent-trend-team",
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
               'border-top':'3px solid #FDB927',
               'border-bottom':'3px solid  #FDB927'
           }
        ),
        dbc.Row(
           [
            dbc.Col(
                [
                html.Div(
                    [
                    html.P(
                    "Stat Type:",
                    style={
                        'color':'white',
                        'padding':'0px 0px 5px 0px',
                        'margin':'30px 0px 0px 0px',
                        'display':'inline-block'
                    }
                ),
                html.P(
                    "Sentiment Type:",
                    style={
                        'color':'white',
                        'padding':'0px 0px 5px 105px',
                        'margin':'15px 0px 0px 0px',
                        'display':'inline-block'
                    }
                ),
                    ]
                ),
                html.Div(
                    [
                    dcc.Dropdown(
                    id="stat-select-team",
                    options=[
                        {'label':'Per Game', 'value':'pg'},
                        {'label':'Per 100 Pos', 'value':'p100'},
                        {'label':'Cumulative', 'value':'cum'}
                    ],
                    value='pg',
                    clearable=False,
                    style={
                        'width':'150px',
                        'padding':'0px 0px 0px 0px',
                        'margin':'0px 30px 0px 0px',
                        'background-color':colors[1],
                        'color':colors[0],
                        'font-color':colors[0],
                        'display':'inline-block'
                        
                    }
                    ),
                    dcc.Dropdown(
                    id="sent-select-team",
                    options=[
                        {'label':'All', 'value':'all'},
                        {'label':'Positive', 'value':'positive'},
                        {'label':'Negative', 'value':'negative'},
                    ],
                    value='all',
                    clearable=False,
                    style={
                        'width':'150px',
                        'padding':'0px 0px 0px 0px',
                        'background-color':colors[1],
                        'color':colors[0],
                        'font-color':colors[0],
                        'display':'inline-block'
                        
                    }
                    ),
                    ]
                ),
                html.Iframe(
                    src='https://www.youtube.com/embed/BqzIdPZLIsg',
                    width='95%',
                    height='80%',
                    style={
                        'padding':'15px 0px 30px 0px'
                    }
                    
                ),
                ],
                width = {'size':4},
                style={
                    'margin':'0px 0px 0px 30px',
                    'font-weight':'bold',
                    'border-right':'3px solid {}'.format(colors[1])
                }
            ),
            dbc.Col(
                [
                html.H3(
                    "Team Statistics",
                    style={
                        'margin':'30px 0px 30px 0px',
                        'font-weight':'bold',
                        'font-size':'28px',
                        'color':'white',
                        'textAlign':'center'
                    }
                ),
                html.Div(
                    id='stats-table-container-team',
                    className='stats-table-container',
                    children=[
                        dash_table.DataTable(
                            id='stats-table-team',
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
                        'padding':'15px 0px 30px 0px'
                    }
                ),
                html.Div(
                    id='stats-table-container-team2',
                    className='stats-table-container',
                    children=[
                        dash_table.DataTable(
                            id='stats-table-team2',
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
                    id='stats-table-container-team3',
                    className='stats-table-container',
                    children=[
                        dash_table.DataTable(
                            id='stats-table-team3',
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
               'padding-right':'15px'
           }
           
        ),
        dbc.Row(
           [
            html.Img(
                    id="wordcloud-team",
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
                dcc.Graph(
                    id="sentiment-rank",
                    style={
                        'textAlign':'center'
                    }
                ),
                ],
                width={'size':4},
                style={
                    'padding':'30px 0px 0px 30px',
                     'border-right':'3px solid {}'.format(colors[1])
                }
            ),
            dbc.Col(
                [
                dcc.Graph(
                    id='top-words-team',
                )
                ],
                width={'size':4},
                style={
                    'margin':'0px 0px 0px 0px',
                    'textAlign':'left',
                    'border-right':'3px solid {}'.format(colors[1])
                }
                
            ),
            dbc.Col(
                [
                dcc.Graph(
                    id='top-emojis-team',
                )
                ],
                width={'size':4},
                style={
                    'margin':'10px 0px 0px 0px',
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
            html.H3(
                "Relative Player Associations",
                style={
                    'color':colors[1],
                    'font-weight':'bold',
                    'textAlign':'center',
                    'padding':'15px 0px 0px 0px'
                }
            ),
            dcc.Graph(
                figure=vs.generate_player_hm(),
                id="sentiment-hm",
                style={
                    'textAlign':'center',
                    'padding-left':'7%',
                    'padding-right':'7%'
                }
            ),
            ],
            style={
               'background-color':colors[0],
               'border-bottom':'3px solid  #FDB927',
               'padding':'0px 0px 30px 0px'
            }
        ),
        dbc.Row(
            [
            dcc.Graph(
                id="sentiment-1-team",
                style={
                        'textAlign':'center',
                        'padding-left':'7%',
                        'padding-right':'7%'
                }
            ),
            ],
            style={
               'background-color':colors[0],
               'border-bottom':'3px solid  #FDB927',
               'padding':'0px 0px 30px 0px'
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
                    id="stat-select-team2",
                    options=[
                        {'label':'Per Game', 'value':'g'},
                        {'label':'Per 100 Pos', 'value':'p100'},
                        {'label':'Cumulative', 'value':'cum'},
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
                    id="stat-select-team3",
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
                    id='sentiment-2-team',
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
                    id=('sent-corr-team'),
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
    Output('record', 'children'),
    Output('rank', 'children'),
    Output('last-ten', 'children'),
    Output('streak', 'children'),
    Output('win-pct', 'children'),
    Input('date-select-team', 'date')
)

def update_header(date):
    team_date = TeamDate("LAL", date=date)

    rec = team_date.get_record()
    seed = team_date.current_seed
    seed = seed.split(' ')[-1]
    last_ten = team_date.get_record(x=10)
    streak = team_date.current_streak()

    x = re.findall(r"(\d{1,2})-(\d{1,2})", rec)
    w = int(x[0][0])
    l = int(x[0][1])

    wpct = w / (w+l)

    if streak[0] == 'W':
        col = 'green'
    else:
        col = 'red'

    return rec, seed, last_ten, html.Span(streak, style={'color': col}), f'{wpct:.3}'

@callback(
    Output('sent-ytd-team', 'children'),
    Output('sent-recent-team', 'children'),
    Output('sent-trend-team', 'children'),
    Input('entity-select', 'value'),
    Input('date-select-team', 'date')
)

def update_sent(ent, date):
    if ent=='team':
        team_date = TeamDate("LAL", date=date)
        sent = team_date.get_sentiment()
        sent_rec, _, diff = team_date.get_trending_sentiment()
    else:
        sent=ss.get_sent_other(ent, date)
        sent_rec, _, diff = ss.get_trending_sentiment(ent, date)

    # color sentiment
    if sent <= 0.1:
        col_sent='red'
    elif sent <= 0.2:
        col_sent='yellow'
    elif sent <= 0.3:
        col_sent='white'
    else:
        col_sent='green'

    # format
    sent = f'{sent:.1%}'
    

    # if not on team anymore, return 0% for recent/trending sentiment
    if sent_rec == 0:
        return html.Span(sent, style={'color': col_sent}), "0%", "0%"
    else:
        sent_rec = sent_rec.round(3) 
        diff = diff.round(3) 
        # color sentiment
        if sent_rec <= 0.1:
            col_rec='red'
        elif sent_rec <= 0.2:
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
            

    return html.Span(sent, style={'color': col_sent}), html.Span(sent_rec, style={'color': col_rec}), html.Span(diff, style={'color': color_trend})

@callback(
    Output('stats-table-team', 'columns'),
    Output('stats-table-team', 'data'),
    Input('date-select-team', 'date'),
    Input('stat-select-team', 'value')
)

def update_table(date, stat):
    team_date = TeamDate("LAL", date=date)
    if stat == 'pg':
        s = team_date.get_per_game_stats()
        suffix = "_PG"
    elif stat == 'p100':
        s = team_date.get_per_p_possessions_stats()
        suffix="_P100P"
    else:
        s = team_date.get_cum_stats()
        suffix = ""

    cols_og = [
        'PTS', 'REB', 'AST', 'STL', 'BLK', 'TO',
        'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'PF', 
        ]
    
    cols = [x + suffix for x in cols_og]
    s = s.to_frame().T #keep 13-14
    s = s[
        cols
    ]
    s.columns=[x.lower().capitalize() for x in cols_og]
    data_dict = s.to_dict('records')
    
    return [{'name': col, 'id': col} for col in s.columns], data_dict


@callback(
    Output('stats-table-team2', 'columns'),
    Output('stats-table-team2', 'data'),
    Input('date-select-team', 'date'),
)

def update_table2(date):
    team_date = TeamDate("LAL", date=date)
    s = team_date.get_per_game_stats()
    s = s.to_frame().T 

    cols_og = [
        'NET_RATING', 'OFF_RATING', 'DEF_RATING', 
        'REB_PCT', 'OREB_PCT', 'DREB_PCT', 'AST_PCT', 'USG_PCT', 'PACE', 'PIE'
    ]

    s = s[
        cols_og
    ]

    s.columns = [
        'NRtg', 'ORtg', 'DRtg', 'RebPct', 'ORebPct', 'DRebPct',
        'AstPct', 'UsgPct', 'Pace', 'PIE',
        
    ]

    data_dict = s.to_dict('records')
    
    return [{'name': col, 'id': col} for col in s.columns], data_dict

@callback(
    Output('stats-table-team3', 'columns'),
    Output('stats-table-team3', 'data'),
    Input('date-select-team', 'date'),
)

def update_table3(date):
    team_date = TeamDate("LAL", date=date)
    s = team_date.get_per_game_stats()
    s = s.to_frame().T 

    cols_og = [
        'TS_PCT','EFG_PCT', 'GAMES', 'FG_PCT', 'FG3_PCT', 'FT_PCT',
        'AST_TOV', 'AST_RATIO'

    ]

    s = s[
        cols_og
    ]

    s.columns = [
        'TsPct', 'EfgPct', 'Games', 'FgPct', 'Fg3Pct', 'FtPct',
        'AstTov', 'AstRat'

    ]

    data_dict = s.to_dict('records')
    
    return [{'name': col, 'id': col} for col in s.columns], data_dict

@callback(
    Output('pie-chart-team', 'figure'),
    Input('entity-select', 'value'),
    Input('date-select-team', 'date'),
    
)

def update_pie_chart(entity, date):
    if entity=='team':
        team_date = TeamDate("LAL", date=date)
        fig = team_date.basic_pie_chart()
        fig.update_layout(
            plot_bgcolor=colors[0],
            paper_bgcolor=colors[0],
        )
    else:
        fig = vs.basic_pie_chart(entity, date)
        fig.update_layout(
            plot_bgcolor=colors[0],
            paper_bgcolor=colors[0],
        )
    
    return fig


@callback(
    Output('wordcloud-team', 'src'),
    Input('entity-select', 'value'),
    Input('sent-select-team', 'value')
)

def update_wordcloud(entity, sent):
    if entity == 'team':
        team_date = TeamDate("LAL")
        wordcloud = team_date.generate_wordcloud()
        img = BytesIO()
        wordcloud.save(img, format='PNG')
    else:
        token_dict = ss.get_token_dict(player_ref=entity, kind=sent)
        wordcloud = vs.generate_wordcloud(token_dict)
        img = BytesIO()
        wordcloud.save(img, format='PNG')
    
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())


@callback(
    Output('top-words-team', 'figure'),
    Input('entity-select', 'value'),
    Input('date-select-team', 'date'),
    Input('sent-select-team', 'value')
)

def update_top_words(entity, date, sent):
    ent_dict = {
        'jeanie_buss':'jeanie',
        'rob_pelinka':'rob',
        'darvin_ham':'ham'
    }
    if entity == 'team':
        team_date = TeamDate("LAL", date=date)
        fig = team_date.plot_top_ten(kind=sent)
    else:
        ent_key = ent_dict[entity]
        fig = vs.plot_top_ten(ent_key=ent_key, kind=sent)

    return fig

@callback(
    Output('top-emojis-team', 'figure'),
    Input('entity-select', 'value'),
    Input('date-select-team', 'date'),
    Input('sent-select-team', 'value')
)

def update_top_emojis(entity, date, sent):
    ent_dict = {
        'jeanie_buss':'jeanie',
        'rob_pelinka':'rob',
        'darvin_ham':'ham'
    }
    if entity == 'team':
        team_date = TeamDate("LAL", date=date)
        fig = team_date.plot_top_ten_emoji(kind=sent)

    else:
        ent_key = ent_dict[entity]
        fig = vs.plot_top_ten_emoji(ent_key=ent_key, kind=sent)

    return fig

@callback(
    Output('sentiment-rank', 'figure'),
    Input('date-select-team', 'date')
)

def update_rank(date):
    fig = vs.plot_ytd_player_sent_ranks(date)

    return fig

@callback(
    Output('sentiment-1-team', 'figure'),
    Input('entity-select', 'value'),
    Input('date-select-team', 'date')
)

def update_sentiment_1(entity, date):
    if entity == 'team':
        team_date = TeamDate("LAL", date=date)
        fig = team_date.plot_sentiment_through_time()
    else:
        fig = vs.plot_sentiment_through_time(player_ref=entity, date=date)
    
    return fig


@callback(
    Output('sentiment-2-team', 'figure'),
    Output('sent-corr-team', 'children'),
    Input('entity-select', 'value'),
    Input('date-select-team', 'date'),
    Input('stat-select-team2', 'value'),
    Input('stat-select-team3', 'value')
)

def update_sentiment_2(entity, date, stat, stat_col):
    if entity == 'team':
        team_date = TeamDate("LAL", date=date)
        fig = team_date.sent_vs_stat(stat_col=stat_col, kind=stat)
        corr = team_date.sent_vs_stat_corr(stat_col, kind=stat)
    
    else:
        fig = ls.sent_vs_wpct(entity, date)
        corr = ls.sent_vs_wpct_corr(entity, date)
    
    if corr < 0:
        col_corr='red'
    else:
        col_corr='green'

    corr = f'{corr:.3}'
    
    return fig, html.Span(corr, style={'color': col_corr})