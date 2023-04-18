import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom

####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/combine')


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
                            "Predictive Modeling with NFL Combine Data",
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
                                    "PDF",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/assets/combine.pdf',
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
                            href='https://github.com/dkjorling/Predictive-Modeling-with-NFL-Combine-Data',
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
                            "The NFL Combine project showcases my proficiency with scikit-learn for machine learning modeling, seaborn for data visualization and statsmodels for statistical analysis. I chose this project because it provided an opportunity to demonstrate a wide range of modeling techniques, and my ability to extract insights from complex data. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "At the NFL Combine, prospective draft picks are measured in height, weight, and arm length, and undergo various physical assessments including bench press and 40-yard dash. Specifically, the project focused on two key questions: 1) Can NFL Combine data be used to determine whether a player is drafted, and 2) For drafted players, can combine data be used to predict draft pick number. To address these questions, I worked with another student to collect and clean the data and trained several predictive models, including logistic regression and a random forest classifier, and regression models such as Linear Regression, Principal Component Regression (PCR), and XGBoost.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "One of the key findings from my analysis was that the relationship between combine results and draft position is much stronger in determining whether a player is drafted or not rather than when they are drafted. This is a valuable insight, as it challenges conventional wisdom and suggests that other factors may play a more significant role in predicting draft position.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "The project also demonstrated my ability to work collaboratively, as I tasked my partner with focusing on the classification task while I focused on the regression task. Together, we were able to apply a range of techniques and tools to the problem and generate valuable insights that can inform decision-making in the sports industry. Overall, my NFL Combine project highlights my skills in data analysis, modeling, and visualization. ",
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
                            "EDA",
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
                html.Div(
                    children=[
                        html.Img(
                            src='assets/position.png',
                            style={
                                'border':'#ae5000 solid 2px',
                                'margin':'15px 15px 0px 0px',
                                'height': '300px',
                                'style':'inline-block'
                                
                            }
                        ),
                        html.Img(
                            src='assets/predictors.png',
                            style={
                                'border':'#ae5000 solid 2px',
                                'margin':'15px 0px 0px 15px',
                                'height': '300px',
                                'style':'inline-block'
                                
                            }
                        ),
                    ],
                    style={
                        'textAlign':'center',
                        'margin':'0px 15px 0px 15px',
                        'background-color':'#faf0e6',
                        'padding':'0px 0px 15px 0px'
                    }
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.P(
                            "I created the two plots above as part of my exploratory data analysis using seaborn. The box plot compares draft pick distributions for each position on the field. Defensive Ends and Tackles, who are often tasked with bringing down the opposing quarterback, have the lowest average draft pick selection. Another interesting insight is that Quarterbacks have a heavily skewed distribution which infers that top-end QBs are extremely valuable but on average the position is actually not drafted very high. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600',
                                'text-align':'left',
                                'padding':''
                            }
                        ),
                        html.P(
                            "The scatterplot matrix shows the response variable plotted against four predictor variables. None of the four variables appear to have too strong of a relationship with draft pick, putting into doubt how strong of a predictor combine results are in determining draft position. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600',
                                'text-align':'left',
                                'padding':''
                            }
                        ),
                        ],
                    )
                    ],
                    style={
                            'margin':'0px 15px 0px 15px',
                            'background-color':'#faf0e6'
                    }
                ),

                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            "Results and Conclusion",
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
                    html.Div(
                        children=[
                            html.Img(
                                src='assets/cm.png',
                                style={
                                    'border':'#ae5000 solid 2px',
                                    'height': '300px',
                                    'margin':'0px 0px 5px 0px'
                                    
                                }
                            ),
                            html.P(
                                "The best performing classifier model was logistic regression which yielded cross-validated accuracy of 65.8% in predicting whether a player is drafted or not. The confusion matrix above displays this result in more detail and can be used to calculate a precision score of 67% and recall of 66%. A random forest classifier was also trained and tuned which produced an accuracy of just 64.2%. Given our somewhat discouraging EDA the moderate accuracy was surprising and shows that combine results are strong indicators of drafted status. ",
                                style={
                                    'font-size':'16px',
                                    'color':'#666600',
                                    'textAlign':'left',
                                    'padding': '5px 0px 0px 0px'
                                }
                            ),

                        ],
                    ),
                    ],
                    style={
                            'textAlign':'center',
                            'margin':'0px 15px 0px 15px',
                            'background-color':'#faf0e6'
                    }
                ),
                html.Div(
                    children=[
                        html.Img(
                            src='assets/pca.png',
                            style={
                                'border':'#ae5000 solid 2px',
                                'margin':'15px 15px 0px 0px',
                                'height': '300px',
                                'style':'inline-block'
                                
                            }
                        ),
                        html.Img(
                            src='assets/xgb.png',
                            style={
                                'border':'#ae5000 solid 2px',
                                'margin':'15px 0px 0px 15px',
                                'height': '30px',
                                'style':'inline-block'
                                
                            }
                        ),
                    ],
                    style={
                        'textAlign':'center',
                        'margin':'0px 15px 5px 15px',
                        'background-color':'#faf0e6',
                        'padding':'0px 0px 0px 0px'
                    }
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.P(
                            "I initialized the regression problem with a statistical model using the statsmodels library. Following a backward selection process, my final model predictors included weight, arm length, forty-yard dash, shuttle and position, and had an adjusted R-squared of 0.084. Although the low R-squared was expected, it was informative to see which variables were statistically significant. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600',
                                'text-align':'left',
                                'padding':'5px 0px 0px 0px'
                            }
                        ),
                        html.P(
                            "I used this information to train a linear regressor with the predictors utilized in the final statistical model, which resulted in a cross-validated RMSE of 67.0 picks. Subsequently, PCA was implemented to reduce dimensionality since the dataset contained many correlated predictors. The first three principal components were then used to train another linear regressor, this time yielding a cross-validated RMSE of just 68.0 picks. Finally, a tree-based ensemble method that combines boosting and regularization called XGBoost was implemented. After tuning various hyper-parameters such as max tree depth and learning rate, the model produced a cross-validated RMSE of just 68.45. Comparing model results to the null model standard deviation of 69.8 suggests that combine statistics are not good predictors of draft position. Despite poor predictive power, the study still revealed the most important predictors, namely forty time and weight, and delivered the insight that combine results act more as a threshold rather than a specific pick predictor. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600',
                                'text-align':'left',
                                'padding':''
                            }
                        )
                        ],
                    )
                    ],
                    style={
                            'margin':'0px 15px 0px 15px',
                            'background-color':'#faf0e6'
                    }
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
                                "Machine Learning with scikit-learn: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Demonstrate breadth of scikit-learn knowledge through training various regression and classification models and implementing preprocessing steps",
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
                                "Data Visualization with seaborn: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Exhibit proficiency with seaborn to create informative and aesthetic visualizations ",
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
                                "Statistical Analysis with statsmodels: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Utilize statsmodels library to implement OLS modeling, residual analysis, and goodness-of-fit testing",
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
                            "Display ability to clearly and concisely state the problem, describe methodologies and communicate results",
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
                            "scikit-learn, seaborn, statsmodels, pandas",
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

