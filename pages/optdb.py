import dash_bootstrap_components as dbc
from dash import html, register_page
from dash_bootstrap_templates import load_figure_template

# my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/optdb')


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
                            "Creating an Options Database and Live Volatility Surface App",
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
                            href='/optdb/dashboard',
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
                            href='https://github.com/dkjorling/Option-DB-and-IV-Surface-Dash',
                            style={
                                'padding':'0px 0px 0px 15px',
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
                            "Through development of an options database and real-time implied volatility surface visualizer, I exhibit proficiency with SQL, AWS RDS and API application integration. Motivation in creating the options database stems from a desire to both learn how to scrape and store large amounts of data and test various inter-asset options strategies. I was also interested in learning how to create a real-time application and created a dashboard that pulls live options information from Yahoo Finance. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "Utilizing both the yahooquery and yfinance python libraries, I wrote a script that automatically pulls stock and options price data 3x daily and uploads it to my AWS MySQL database. Collected data includes price and volume information for approximately 300 underlying assets and their respective option chains. The database includes 4 tables: stocks, containing each asset name, stock prices, containing 3x daily price data for stocks, options, containing descriptions of each option contract, and option prices, containing option price data recorded simultaneously with stock prices. To ensure validity of inter-asset analysis, I prioritized upload speed by adapting thread pooling for concurrent API calls and pandas for bulk SQL inserts. This resulted in an optimized script that pulls and uploads approximately 300,000 rows of data in under one minute. In the future the collected data will be used to test a multitude of inter-asset options strategies based on my Master’s thesis research. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "The real-time implied volatility dashboard pulls live options data from yahoo finance and displays a 3D surface visualization representing an asset’s implied volatility surface. Two additional plots display implied volatility through strike space, given an expiration, and through expiration space, given a strike price. Eventually I plan on creating additional analysis tools that pull data directly from my options database. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        )
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
                        [
                        html.H2(
                            "Skill Highlights",
                            style={
                                'font-size':'22px',
                                'color':'#666600'
                            }
                        ),
                        html.Ul(
                            [
                            html.Li(
                                html.Div(
                                    [
                                    html.Span(
                                        "SQL Database Design:  ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Design an intricate and logical database with tables that utilize foreign keys for seamless inter-table interaction. ",
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
                                        "Optimal API Usage and DB Data Insertion: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Develop a script that utilizes thread pooling and bulk SQL insertion to maximize upload speed. ",
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
                                        "AWS RDS: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Initialize an AWS MySQL Database instance to efficiently store, access and share data. ",
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
                                        "Data Visualization: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Produce eye-popping 3D visuals based on real-time data using plotly GO. ",
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
                                    "SQLAlchemy, yfinance, yahooquery, pandas, apcheduler, plotly, Dash",
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
                            }
                        )
                        ],
                        style={
                            'margin':'15px 30px 0px 30px',
                            'background-color':'#faf0e6',
                        }
                    ),
                    ],

                ),
                
                dbc.Row(
                    style={
                        'background-color':'seashell',
                        'height':'300px',   
                        'width':'110%'
                    }
                )
            ],
            style={
                'background-color':'seashell',

            }
        ),
        page_bottom(),
     ],
     style={
         'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
     }
)


