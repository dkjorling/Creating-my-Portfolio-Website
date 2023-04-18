import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/optionsport')


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
                            "Building an Options Portfolio with Deep Learning",
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
                            href='/optionsport/dashboard',
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
                            href='https://github.com/dkjorling/Building-an-Options-Portfolio-with-Deep-Learning',
                            style={
                                'padding':'0px 15px 0px 15px',
                                'textAlign':'center'
                            }
                        ),

                        html.A(
                            html.Button(
                                    "PDF",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/assets/thesis.pdf',
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
                            "My Master's Thesis aimed to combine my passion for deep learning architectures with my expertise in financial derivatives. While deep learning has been extensively researched for stock-based portfolios, there is a lack of literature on inter-asset options strategies. To fill this gap, I created a proof-of-concept Options Portfolio that takes daily long/short implied volatility positions in 315 underlying securities, leveraging the state-of-the-art Transformer Model as a foundation - the same model used in Chat GPT.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "To account for the difficulty in collecting enough price data to train complex deep learning models, I used implied volatility data as a proxy for direct straddle prices. I trained various end-to-end deep learning models that directly maximize the Sharpe Ratio, a popular portfolio performance metric that is easily differentiable and thus usable in back propagation. This approach contrasts with traditional two-step portfolio optimization methods that first estimate asset returns and covariances before solving a constrained optimization problem.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "I implemented an expanding training window approach, using the first X years as a training set, the next year as a validation set, and the following year as a test set. I re-trained the model each year after tuning various hyperparameters using the train and validation sets. The model was then evaluated on the unseen test data, yielding the results shown below. Although costs were ignored for simplicity's sake, the Options Portfolio significantly outperformed all baselines and showed tremendous potential for use in an actual trading strategy.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "As a final touch, I created an interactive dashboard to visualize my data and results. This goes beyond the scope of the thesis requirements, but I wanted to provide a comprehensive and user-friendly way to understand the portfolio's performance.",
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
                
                dbc.Row([
                    dbc.Col(
                        html.H2(
                            "Results",
                            style={
                                'font-size':'22px',
                                'color':'#666600'
                            }
                        ),
                        style={
                            'margin':'0px 30px 0px 30px',
                            'background-color':'#faf0e6'
                            }
                    )
                    
                ]),
                
                dbc.Row(
                    [
                    dbc.Col(
                        html.Div(
                            children=[
                                html.Img(
                                    src='assets/results_tab.png',
                                    style={
                                        'font-size':'22px',
                                        'border':'#ae5000 solid 2px',
                                        'margin':'15px'
                                    }
                                ),
                                html.P(
                                    "The Options Portfolio outperforms the three baseline models (Equal-Weighted Long Portfolio, GRU, LSTM) in nearly every category. While the GRU and LSTM portfolios have slightly lower variance, this is more than offset by the substantially higher returns produced by the Options Portfolio. Impressively, the Options Portfolio has both the lowest average max-drawdown and the highest annual return, to yield a Calmar Ratio–the preferred metric for hedge-fund performance–more than double that of the GRU model, and 44 times higher than the equal-weighted portfolio.",
                                    style={
                                        'font-size':'16px',
                                        'color':'#666600',
                                        'textAlign':'left'
                                    }
                        ),

                            ],
                        
                        ),
                        style={
                            'margin':'0px 30px 30px 30px',
                            'background-color':'#faf0e6',
                            'textAlign':'center'
                            
                        }
                    )
                    
                    ]
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.H2(
                            "The Options Portfolio Model Diagram",
                            style={
                                'font-size':'22px',
                                'color':'#666600',
                                'textAlign':'left'
                            }
                        ),
                        html.Div(
                            children=[
                                html.Img(
                                    src='assets/neural.png',
                                    style={
                                        'border':'#ae5000 solid 2px',
                                        'margin':'15px',
                                        'height': '500px'
                                    }
                                )
                            ],
                        
                        ),
                        ],
                        style={
                            'margin':'15px 30px 30px 30px',
                            'background-color':'#faf0e6',
                            'textAlign':'center'
                            
                        }
                    )
                    
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
                                        "Deep Learning with PyTorch: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Display robust deep learning knowledge through design of various complex end-to-end models, training and tuning model hyperparameters, and evaluating performance on unseen testing data. ",
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
                                        "Time Series Analysis: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Show mastery of ML time series techniques, implementing a 30-day lookback window with 10 features for 315 assets and an expanding window training approach to maximize breadth of data utilization. ",
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
                                        "Analytical Writing: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Demonstrate strong written skills through breaking down highly complex concepts across different disciplines and effectively communicating these ideas to broad audiences. ",
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
                                    "Create visuals that are intricately designed, highly informative and aesthetic including a model diagram and various plotly graphs. ",
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
                                    "PyTorch, pandas, plotly, Dash",
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

                        ),
                        ],
                        style={
                                'margin':'0px 30px 0px 30px',
                                'background-color':'#faf0e6',
                                'list-style-type':'square',
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
