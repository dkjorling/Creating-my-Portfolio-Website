import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/nflwinner')


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
                            "Building a Winner in the Modern NFL",
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
                                    "PDF",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/assets/nflwinner.pdf',
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
                            href='https://github.com/dkjorling/Building-a-Winner-in-the-Modern-NFL',
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
                            "'Building a Winner in the Modern NFL' is a project that showcases my expertise in end-to-end statistical analysis using R. The project involves data collection with rvest, data cleaning and analysis with tidyverse, OLS and GAM modeling, and data visualization with ggplot. In the NFL, decision-makers must allocate limited salary cap and draft pick capital to maximize winning percentage. This project aimed to identify optimal resource allocation strategies, such as whether teams should extend their own players or spend in free agency, if trading draft picks for players adds value, and if there are on-field position groups that should be prioritized.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "To achieve this goal, I sourced data primarily from Spotrac, which provided information related to salary cap allocation by position, and complete draft and transaction history. The study spanned 2013-2021 for all 32 teams and utilized a draft-pick value chart to assign the worth of each pick accurately. Additionally, I sourced average team age data to determine whether there is an optimal average roster age. In creating and analyzing this robust dataset, I aimed to uncover insights that can inform decision-making for NFL teams looking to build a winning team in the modern era.",
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
    
                    ],
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
                            'margin':'0px 30px 0px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
                    ]
                ),
                dbc.Row(
                    [
                    html.Div(
                        children=[
                            html.Img(
                                src='assets/nflweda1.png',
                                style={
                                    'border':'#ae5000 solid 2px',
                                    'height': '300px',
                                    'margin':'0px 0px 5px 0px'
                                    
                                }
                            ),
                            html.P(
                                "The bar plot displays salary cap and draft pick allocation for each on-field position. While most positions are allocated similarly between salary cap and draft resources, significantly more draft capital is used on Defensive linemen (DL) secondary (SEC) and running backs (RB) than salary space. Additionally, special teams players (ST) are nearly never drafted with valuable picks.",
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
                            src='assets/nflweda2.png',
                            style={
                                'border':'#ae5000 solid 2px',
                                'margin':'15px 15px 0px 0px',
                                'height': '220px',
                                'style':'inline-block'
                                
                            }
                        ),
                        html.Img(
                            src='assets/nflweda3.png',
                            style={
                                'border':'#ae5000 solid 2px',
                                'margin':'15px 0px 0px 15px',
                                'height': '220px',
                                'style':'inline-block'
                                
                            }
                        ),
                    ],
                    style={
                        'textAlign':'center',
                        'margin':'0px 15px 0px 15px',
                        'background-color':'#faf0e6',
                        'padding':'0px 0px 5px 0px'
                    }
                ),    
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.P(
                            "The scatterplots show the linear relationship between the response variable, regular-season win percentage, and two predictor variables: total spending and normalized free agency spending. While total spending has a strong positive relationship with winning percentage, free-agency spending is surprisingly negatively correlated with the response, indicating that it is often not beneficial to team performance. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600',
                                'padding': '5px 0px 0px 0px'
                            }
                        ),
                        ],
                        style={
                            'margin':'0px 30px 15px 30px',
                            'background-color':'#faf0e6'
                        }
                    ),
    
                    ],
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
                            'margin':'0px 30px 0px 30px',
                            'background-color':'#faf0e6'
                            }
                    )
                    ]
                ),
                dbc.Row(
                    [
                    html.Div(
                        children=[
                            html.P(
                                "I initially implemented OLS modeling which yielded a final model including total spend, free agency spend, trades made, average age, and linebacker draft proportion. The model resulted in an R-squared of 0.165, with nearly half of that number attributed to total spend. A disappointing finding was that there appeared to be no advantage in allocating salary cap or draft capital to certain positions, as only the linebacker draft proportion variable was statistically significant. This suggests that building a winning roster requires identifying and securing talent at all positions.",
                                style={
                                    'font-size':'16px',
                                    'color':'#666600',
                                    'textAlign':'left',
                                    'padding': '5px 0px 5px 0px'
                                }
                            ),
                            html.P(
                                "Next, I fit a GAM using kernel regression which yielded an RMSE of .1609 compared to null standard deviation of .1919. The RMSE/SD ratio of the GAM was comparable to the OLS R-squared, and therefore the OLS model was selected as the final model due to its easier interpretability. Although the study did not uncover many insights related to optimal position allocation, it did reveal high total spend, low free agency spend and high number of trades as important factors in predicting win percentage. Additionally, the study suggests that linebackers are undervalued in the NFL draft. One potentially interesting extension of this study would be analyzing playoff performance instead of regular season performance.",
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
                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            "Skill Highlights [R]",
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
                                "Web Scraping with rvest: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Scrape data with rvest library including using forms to grab data behind account paywall",
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
                                "Data Analysis with tidyverse: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Clean, extract and engineer features, and analyze data using tidyvere library",
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
                                "General Additive Modeling: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Fit GAM using kernel regression, beginning with most predictive variable and iteratively regressing on prior variable residuals ",
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
                                "Data Visualization with ggplot: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Create informative and aesthetic visuals with ggplot library",
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
                            "Thoroughly describe the problem and explain entirety of the data analysis process in clear language ",
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
                            "rvest, tidyverse, ggplot",
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
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                'background-color':'seashell'
            }
        ),
        page_bottom(),
    ]
)
