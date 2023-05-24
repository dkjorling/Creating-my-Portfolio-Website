import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

# my impots
from dash_helpers import proj_buttons2, proj_buttons3, proj_image, page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/portfolio')


load_figure_template('FLATLY')

### Begin Page Layout ###

layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                html.Br(),
                
                dbc.Row(
                    html.H2(
                        [
                        html.U(
                        "Portfolio"
                        ),
                        ],
                        style={
                            'font-size':'30px',
                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                            'font-weight':'bold',
                            'color':'#ae5000'
                        }
                    ),
                    style={
                        'margin':'0px 30px 0px 30px',
                        }
                ),
                
                dbc.Row(
                    html.P(
                        "From utilizing Deep Learning to generate financial alpha to using Machine Learning algorithms to identify competitive advantages in the NFL to applying Sentiment Analysis to Reddit comments, my portfolio not only showcases my abilities as a data scientist but also represents topics I am truly passionate about. Each project can be read about in greater detail by clicking the “Overview” button, while “Code” links directly to a project’s Github repository. Finally, many of my projects are supplemented with an interactive dashboard which can be accessed by clicking “Dashboard”. ",
                        style={
                            'font-size':'16px',
                            'color':'#666600'
                        }
                    ),
                    style={
                        'margin':'0px 30px 15px 30px',
                        'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                        'background-color':'#faf0e6'
                        }
                ),
                
                dbc.Row([
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "Building an Options Portfolio with Deep Learning",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "UCLA MASTER'S THESIS: Apply state of the art Deep Learning Architectures to over 15 years and 300 tickers worth of daily implied volatility data to create the novel actively managed Options Portfolio.",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            
                            proj_image('finance.png', height='84%', width='84%'),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [Python]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "Deep Learning, Time Series Analysis, Data Visualization",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons3("/optionsport", "https://github.com/dkjorling/Building-an-Options-Portfolio-with-Deep-Learning", "/optionsport/dashboard"),
                            
                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 15px 15px 40px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                        }
                    ),
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "Entity-Level Sentiment Analysis with Reddit Data",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "Pull all Reddit posts/comments from r/lakers dating to beginning of season; Identify player entities and analyze sentiment for each player through time; Create app showing sentiment with player/team stats throughout the season",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            
                            proj_image('lakers.png', '90%', '90%'),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [Python]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "Entity Recognition, Sentiment Analysis, Web Scraping ",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons3("/redditnlp", "https://github.com/dkjorling/Entity-Level-Sentiment-Analysis-with-Reddit-Data", "/redditnlp/dashboard"),
                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 40px 15px 15px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                    ],
                    style={
                        'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    }
                ),
                dbc.Row([
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "IMDb Data Analysis",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "What factors are most important in determining box-office profitability? Scrape data for over 5000 movies using IMDb API; Train/Test Fully Connected Neural Network to predict Box Office Profit; Develop Estimated Profit Generator Dashboard",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            
                            proj_image("imdb_im.png"),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [Python]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "Feature Engineering, Front-End Development, Supervised ML",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons3("/imdb", "https://github.com/dkjorling/IMDB-Dashboard", "/imdb/dashboard"),
                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 15px 15px 40px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "Creating an Options Database and Live Volatility Surface App",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "Design multi-table AWS MYSQL Database; Automatically pull stock/option price data from Yahoo Finance and upload nearly 1 million rows of data to DB daily; Create a real-time volatility surface dashboard.",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            
                            proj_image('aws.png'),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [SQL, AWS, Python]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "Database Design, Web Scraping",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons3("/optdb", "https://github.com/dkjorling/Option-DB-and-IV-Surface-Dash", "/optdb/dashboard"),
                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 40px 15px 15px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                    ],
                    style={
                        'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
                    }
                ),
                dbc.Row([
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "Predictive Modeling with NFL Combine Data",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "Are NFL Combine stats predictive of draft position? Use Logistic Regression/Random Forest to predict drafted/not drafted status based on combine data; Use PCR, XGBoost and Linear Regression to predict draft position using combine data",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px',
                                   }
                            ),
                            
                            proj_image('combine.png', '75%', '75%'),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [Python]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "ML Classification, Supervised Learning, Dimensionality Reduction",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons3("/combine", "https://github.com/dkjorling/Predictive-Modeling-with-NFL-Combine-Data", "/assets/combine.pdf", button3="PDF")
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 15px 15px 40px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                   
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "Building a Winner in the Modern NFL",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "What is the optimal way to spend NFL Salary/Draft Resources? Analyze Salary Cap and Draft Capital Resource Allocation by Position; Statistical Regression using Linear Model and GAM Kernel Regression ",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            
                            proj_image('bengals.png', height='89%', width='89%'),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [R]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "EDA, Statistical Inference, Linear Modeling, General Additive Model",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons3("nflwinner", "https://github.com/dkjorling/Building-a-Winner-in-the-Modern-NFL", "/assets/nflwinner.pdf", button3="PDF"),
                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 40px 15px 15px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                    ],
                    style={
                        'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
                    }
                ),
                dbc.Row([
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "Creating my Portfolio Website",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center',
                                    'font-weight':'bold'
                                }
                            ),
                            html.P(
                                "Utilize Plotly Dash to design website; create and embed various dashboards for individual projects; Deploy website using AWS Elastic Beanstalk.",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            
                            proj_image('web.png', height='85%', width='85%'),
                            
                            html.Div([
                                html.Span(
                                    "SKILLS [Python, AWS]: ",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "AWS Elastic Beanstalk, Plotly Dash, Web Design",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            
                            proj_buttons2("/website", "https://github.com/dkjorling/Creating-my-Portfolio-Website"),
                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 15px 30px 40px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                    dbc.Col(
                        dbc.Stack([
                            html.H4(
                                "",
                                style={
                                    'color':'#ae5000',
                                    'padding':'10px 10px 0px 10px',
                                    'font-size':'18px',
                                    'textAlign':'center'
                                }
                            ),
                            html.P(
                                "",
                                style={
                                    'color':'#666600',
                                    'font-size':'12px',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            

                            
                            html.Div([
                                html.Span(
                                    "",
                                    style={
                                        'color':'#004640'
                                    },
                                ),
                                "",
                                ],
                                style={
                                    'color':'#ae5000',
                                    'font-size':'12px',
                                    'textAlign':'center',
                                    'padding':'5px'
                                }
                            ),
                            

                            
                        ]),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'15px 40px 30px 15px',
                            'width':'50%',
                            'border':'1px solid #666600',
                            'textAlign':'center'
                                }
                    ),
                ],
                style={
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
                }
            ),
            
            dbc.Row(
                style={
                    'padding':'0px 0px 300px 0px'
                    }
            )
                
            ],
            style={
                'background-color':'seashell'
            }
        ),
        page_bottom(),
    ]
)

