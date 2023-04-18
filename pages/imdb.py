import dash_bootstrap_components as dbc
from dash import html, register_page
from dash_bootstrap_templates import load_figure_template

# my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/imdb')


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
                            "IMDb Data Analysis",
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
                    ],
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
                            href='/imdb/dashboard',
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
                            href='https://github.com/dkjorling/IMDB-Dashboard',
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
                            href='assets/imdb.pdf',
                            style={
                                'padding':'0px 0px 0px 15px',
                                'textAlign':'center'
                            }
                        ),
                        
                    
                    ],
                    style={
                        'padding':'15px 0px 15px 0px',
                        'textAlign':'left',
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
                            "The IMDb Analysis project is an excellent demonstration of my expertise in the complete data science pipeline, from data collection and cleaning to feature engineering, modeling, visualization, and front-end integration. My teammates and I scraped data using the IMDb API to build a comprehensive dataset of over 5,000 films, including data on genre, stars, awards, and plot summaries. Each team member was responsible for either conducting general EDA or modeling specific aspects of the data, while also creating a user-facing dashboard with real-world applications. In my case, I focused on training a fully-connected neural network to predict inflation-adjusted box office profit and integrating it into a user-friendly app.",
                        ),
                        html.P(
                            "As part of my responsibilities, I volunteered to clean the data and engineer features to create a robust final dataset for the whole team to use. My cleaning process involved removing films without budget or gross revenue data, extracting all awards won by parsing the 'awards' category, and converting any monetary variables to 2022 dollars for valid comparison across different time periods. To reduce model complexity and eliminate categories with few datapoints, I also condensed certain categorical variables such as ratings and genres. Additionally, I found that the release date of a film could be predictive of gross profit, so I created four 'time of year' categories as an additional predictor. Finally, I created numerical variables for star actors, actresses, directors, and writers, based on their frequency of appearances in the dataset called 'star power,' 'director popularity,' and 'writer popularity'. I inferred that these variables could serve as strong predictors of box office profits.",
                        ),
                        html.P(
                            "To build the neural network, I utilized the PyTorch framework, fine-tuning and optimizing the model until I achieved the best performance possible. I then integrated the trained model into a Plotly Dash application, creating a user-friendly interface that movie executives could use to estimate film profits based on various inputs. Our team also created an EDA dashboard, including sentiment analysis, and a movie generator dashboard that allows users to type in a phrase and receive a list of films that match the phrase. More details of the entire project are available in the attached PDF file.",
                        ),
                        ],
                        style={
                            'margin':'0px 30px 15px 30px',
                            'background-color':'#faf0e6',
                            'font-size':'16px',
                            'color':'#666600'
                        }
                    ),
    
                    ]
                ),
                
                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            "Results",
                            style={
                                'font-size':'22px',
                                'color':'#666600'
                            }
                        ),
                        style={
                            'margin':'15px 30px 0px 30px',
                            'background-color':'#faf0e6'
                        }
                    )
                    ]
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.P(
                            "The fully-connected neural network consisted of a 21-node input layer, two hidden layers with 50 and 100 nodes respectively and an output layer yielding the final box office profit prediction.  After splitting the data, I tuned various hyper-parameters on the training set before validating the model on the unseen test data. The final model was trained with the Adam optimizer, using a learning rate of 0.0001 and a batch size of 64 while running through 150 epochs. "
                        ),
                        html.P(
                            "The model produced an RMSE of $250M compared to a null model standard deviation of $290M. While the model is not substantially predictive, several valuable insights were gained by the study. In terms of feature importance, budget was the best predictor of profit while star power and writer popularity were amongst the next best. Furthermore, the results imply that other factors not explained by the data are perhaps more important in explaining box office performance.  "
                        ),
                        ],
                        style={
                            'margin':'0px 30px 15px 30px',
                            'background-color':'#faf0e6',
                            'font-size':'16px',
                            'color':'#666600'
                        }
                    )
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
                                "Data Cleaning: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Efficiently transform raw data into an easily usable dataset and show proficiency with regex via extraction of various awards features from raw strings with varying patterns. ",
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
                                "Feature Engineering: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Show strong critical thinking skills leading to the creation of features that greatly contribute to the final model. ",
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
                                "Supervised Machine Learning: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Display robust knowledge of supervised learning tasks using both categorical and numerical predictors with implementation of one-hot encoding and data normalization to properly utilize all data types. ",
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
                                "Model-UI Integration: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Successfully integrate a trained back-end model into an aesthetic dashboard and engineer an engaging app that gives users nearly limitless input combinations. ",
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
                )
            ],
            style={
                'margin':'15px 0px 0px 0px',
            }
        ),
        page_bottom(),
    ],
    style={
        'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
        'background-color':'seashell',
    }
)
