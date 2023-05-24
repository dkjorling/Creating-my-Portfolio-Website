import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom

####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/cv')


load_figure_template('FLATLY')

layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                dbc.Row(
                    [
                    dbc.Col(
                        html.H1(
                            "CURRICULUM VITAE",
                            style={
                                'font-size':'36px',
                                'color':'white',
                                'font-weight':'bold',
                            }
                        ),
                        style={
                            'margin-left':'5%',
                            'margin-right':'5%'

                        }
                    ),
                    ],
                    style={
                        'background-color':'#ae5000',
                        'border-bottom':'2px solid #004640'
                    }
                ),
                html.Div(
                    [
                    dbc.Row(
                        html.H4(
                            "CORE COMPETENCIES & AREAS OF EXPERTISE",
                            style={
                                'color':'#666600',
                                'font-weight':'bold',
                                'margin-top':'10px',
                                'margin-bottom':'-10px'
                            }
                        )
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            [
                            html.Ul(
                                [
                                html.Li(
                                    "Machine Learning with Python"
                                ),
                                html.Li(
                                    "Statistical Modeling with R"
                                ),
                                html.Li(
                                    "Quantitative Problem Solving"
                                )
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                    'font-weight':'bold'
                                }
                                
                            ),
                            ],
                            style={
                                'width':'33%'
                            }
                        ),
                        dbc.Col(
                            [
                            html.Ul(
                                [
                                html.Li(
                                    "Quantitative Finance"
                                ),
                                html.Li(
                                    "Analytical Writing"
                                ),
                                html.Li(
                                    "Statistical Inference"
                                )
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                    'font-weight':'bold'
                                }
                                
                            ),
                            ],
                            style={
                                'width':'34%'
                            }
                        ),
                        dbc.Col(
                            [
                            html.Ul(
                                [
                                html.Li(
                                    "Derivatives Trading"
                                ),
                                html.Li(
                                    "Deep Learning Modeling"
                                ),
                                html.Li(
                                    "Data Management with SQL"
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                    'font-weight':'bold'
                                }
                                
                            ),
                            ],
                            style={
                                'width':'33%'
                            }
                        ),
                        ],
                        style={

                        }
                    ),
                    ],
                    style={
                        'margin-left':'5%',
                        'margin-right':'5%',
                    }
                ),
                html.Hr(
                    style={
                        'border-width':'3px',
                        'width':'90%',
                        'color':'#ae5000',
                        'margin-left':'5%',
                        'margin-right':'5%',
                        'opacity':'unset'
                    }
                ),
                html.Div(
                    [
                    dbc.Row(
                        html.H4(
                            "CODING SUMMARY",
                            style={
                                'color':'#666600',
                                'font-weight':'bold',
                                'margin-top':'10px',
                                'margin-bottom':'-10px'
                            }
                        )
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Python (3+ Years)",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#ae5000',
                            }
                        ),
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                html.Div(
                                    [
                                    html.Span(
                                        "Data Collection/Cleaning/Analysis:  ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Advanced: requests, pandas, numpy, regex, SQLAlchemy; Proficient: nltk",
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
                                        "Modeling: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Advanced: scikit-learn, pyTorch; Proficient: statsmodels, keras, tensorflow, scikit-image, spaCy, vaderSentiment, scipy",
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
                                        "Visualization: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Advanced: matplotlib, plotly, Dash; Proficient: seaborn",
                                    ],
                                    style={
                                        'color':'#ae5000',
                                        'font-size':'16px',
                                        'textAlign':'left',
                                        'padding':'5px',
                                        
                                    }
                                ),
                            ),
                            ],
                        ),
                        ],
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "R (2+ Years)",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#ae5000',
                            }
                        ),
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                html.Div(
                                    [
                                    html.Span(
                                        "Data Collection/Cleaning/Analysis: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Advanced: tidyverse; Proficient: rvest, RMySQL, tm",
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
                                        "Modeling: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Advanced: stats base packages, Proficient: MASS, caret",
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
                                        "Visualization: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Advanced: ggplot2, Proficient: base R plot",
                                    ],
                                    style={
                                        'color':'#ae5000',
                                        'font-size':'16px',
                                        'textAlign':'left',
                                        'padding':'5px',
                                        
                                    }
                                ),
                            ),
                            ],
                        ),
                        ],
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Miscellaneous",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#ae5000',
                            }
                        ),
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                html.Div(
                                    [
                                    html.Span(
                                        "SQL: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Proficiency using SQL, particular knowledge of database design, data insertion and general querying",
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
                                        "Git/Github: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Proficiency using both git and github",
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
                                        "AWS: ",
                                        style={
                                            'color':'#004640',
                                            'font-weight':'bold'
                                        },
                                    ),
                                    "Have set up instances for RDS, Elastic Beanstalk, Lambda, and EC2",
                                    ],
                                    style={
                                        'color':'#ae5000',
                                        'font-size':'16px',
                                        'textAlign':'left',
                                        'padding':'5px',
                                        
                                    }
                                ),
                            ),
                            ],
                        ),
                        ],
                    ),
                    
                    ],
                    style={
                        'margin-left':'5%',
                        'margin-right':'5%',
                    }

                ),
                html.Hr(
                    style={
                        'border-width':'3px',
                        'width':'90%',
                        'color':'#ae5000',
                        'margin-left':'5%',
                        'margin-right':'5%',
                        'opacity':'unset'
                    }
                ),
                html.Div(
                    [
                    dbc.Row(
                        html.H4(
                            "STATISTICS OVERVIEW",
                            style={
                                'color':'#666600',
                                'font-weight':'bold',
                                'margin-top':'10px',
                                'margin-bottom':'-10px'
                            }
                        )
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            [
                            html.Ul(
                                [
                                html.Li(
                                    "OLS and General Linear Model"
                                ),
                                html.Li(
                                    "Logistic Regression"
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                    'font-weight':'bold'
                                }
                                
                            ),
                            ],
                            style={
                                'width':'33%'
                            }
                        ),
                        dbc.Col(
                            [
                            html.Ul(
                                [
                                html.Li(
                                    "Hypothesis Testing"
                                ),
                                html.Li(
                                    "General Additive Modeling (GAM)"
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                    'font-weight':'bold'
                                }
                                
                            ),
                            ],
                            style={
                                'width':'34%'
                            }
                        ),
                        dbc.Col(
                            [
                            html.Ul(
                                [
                                html.Li(
                                    "Causal Inference & Experimental Design"
                                ),
                                html.Li(
                                    "Probability Modeling and Markov Chains"
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                    'font-weight':'bold'
                                }
                                
                            ),
                            ],
                            style={
                                'width':'33%'
                            }
                        ),
                        ],
                        style={

                        }
                    ),
                    ],
                    style={
                        'margin-left':'5%',
                        'margin-right':'5%',
                    }

                ),
                html.Hr(
                    style={
                        'border-width':'3px',
                        'width':'90%',
                        'color':'#ae5000',
                        'margin-left':'5%',
                        'margin-right':'5%',
                        'opacity':'unset'
                    }
                ),
                html.Div(
                    [
                    dbc.Row(
                        [
                        html.H4(
                            "PROFESSIONAL EXPERIENCE",
                            style={
                                'color':'#666600',
                                'margin-top':'10px',
                                'font-weight':'bold',
                            }
                        ),
                        html.Hr(
                            style={
                                'border-width':'2px',
                                'width':'86%',
                                'color':'#666600',
                                'opacity':'unset',
                                'margin-left':'7%',
                                'margin-right':'7%',
                            }
                        ),
                        html.H5(
                            "Belvedere Trading",
                            style={
                                'color':'#666600',
                                'font-weight':'bold'
                            }
                        ),
                        ],
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Portfolio Manager (Precious Metals)",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640',
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Mar 2019 - Sep 2022"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#004640'
                            }
                        )
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                "Exceeded P&L target in each year as Head of Complex, generating a total of over $20M in trading profit over a 3.5-year period"
                            ),
                            html.Li(
                                "Executed high-level decisions combining trading experience, product expertise and a data-driven approach in order to maximize profit and limit risk exposure for the firm's gold and silver desks"
                            ),
                            html.Li(
                                "Achieved numerous impactful quarterly projects including developing a stock-future arbitrage strategy, systematizing scenario-based input correlations, and automating electronic trading sizes and widths. Many of these projects were subsequently adopted by other desks across the firm"
                            ),
                            html.Li(
                                "Generated python scripts in Jupyter Notebook used to maximize current trading strategy profitability and to identify new opportunities "
                            ),
                            html.Li(
                                "Optimized thousands of inputs used in Belvedere's option pricing model related to valuation fitting, scenario analysis, and event importance, and thoroughly explained the reasoning behind these adjustments to the other four desk members"
                            ),
                            html.Li(
                                "Actively participated in weekly meetings with other position managers, where firm-wide challenges and opportunities were discussed, and both short-term and long-term solutions were devised"
                            ),
                            html.Li(
                                "Headed Belvedere's Applications program from March 2018 to September 2022. Lead the firm's in-house software education program through creating and structuring content, selecting and training course instructors and attending weekly meetings with the two other department heads in order to iteratively improve the firm's educational program as a whole"
                            ),
                            html.Li(
                                "Selected as a member of the firm’s 20-person recruiting team from September 2014-September 2020 with key duties including one-on-one first round interviews, leading the mock trading super day assessment and having a large input in determining which candidates the firm extended offers to"
                            ),
                            ],
                            style={
                                'list-style-position':'outside',
                                'list-style-type':'square',
                                'color':'#ae5000',
                                'textAlign':'left',
                            }
                            
                        ),
                        ]
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Product Owner (Roboto Team)",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Nov 2018 - Sep 2020"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#004640'
                            }
                        )
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                "Acted as the primary trader-facing liaison for the Roboto technology team, which developed and maintained all pieces of firm software related to automatically adjusting option-model values"
                            ),
                            html.Li(
                                "Developed presentations and lead educational meetings explaining new automated technologies to the firm's trading team"
                            ),
                            html.Li(
                                "Represented the firm's trading team in monthly Roboto strategy meetings alongside developers and company stakeholders, and contributed to identifying, evaluating, and prioritizing future team projects"
                            ),
                            html.Li(
                                "Ensured trader-based feedback was consistently relayed to developers so that projects were completed efficiently and accurately"
                            ),
                            html.Li(
                                "Participated in new technology alpha-testing on the trading desk prior to firm-wide release, providing feedback used to make changes needed to ensure majority adoption upon final release"
                            ),
                            html.Li(
                                "Effectively communicated the benefits of newly released technology and encouraged implementation across the firm"
                            ),
                            ],
                            style={
                                'list-style-position':'outside',
                                'list-style-type':'square',
                                'color':'#ae5000',
                                'textAlign':'left',
                            }
                            
                        ),
                        ]
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Senior Derivatives Trader(Natural Gas)",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "May 2016 - Feb 2019"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#004640'
                            }
                        )
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                "Executed 75% of the desk's trading volume in both broker and electronic markets"
                            ),
                            html.Li(
                                "Constantly voiced ideas and opinions related to positional risk management and trading strategies, even in situations where the position manager had an opposing view, which contributed to passionate discourse and a collaborative environment on the desk"
                            ),
                            html.Li(
                                "Successfully managed the entirety of desk operations when the Position Manager was out-of-office, taking on added responsibilities including adjusting model values, actively communicating and coordinating with the other 3 traders on the desk, and managing the desk's risk exposure"
                            ),
                            html.Li(
                                "Introduced and researched ideas regarding implementation of profit-generating strategies outside of the desk's core area of expertise, including levered ETF option arbitrage, seasonality strategies and futures-ETF arbitrage, the last of which was profitably used in production"
                            ),
                            html.Li(
                                "Trained and mentored junior traders on the desk through constant discussion and quizzing to prepare them for both theoretical and mock trading assessments"
                            ),
                            ],
                            style={
                                'list-style-position':'outside',
                                'list-style-type':'square',
                                'color':'#ae5000',
                                'textAlign':'left',
                            }
                            
                        ),
                        ]
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Derivatives Trader(S&P 500)",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Apr 2015 - Apr 2016"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#004640'
                            }
                        )
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                "CBOE floor trader specializing in SPX options open-outcry trading as a member of the firm's largest and most profitable desk"
                            ),
                            html.Li(
                                "Provided market liquidity and transparency by quickly and accurately laying two-sided markets for various option structures"
                            ),
                            html.Li(
                                "Contributed thoughtful insights and opinions during daily desk discussions regarding position management and daily trading goals"
                            ),
                            html.Li(
                                "Product Expert for the firm’s trader interface technology team from Mar 2016 to Oct 2018. Created and updated proprietary technology documentation, formally educated all traders on the latest software released by the team, and met weekly with tech team members to discuss necessary improvements to current software and prioritize new technologies  "
                            ),
                            ],
                            style={
                                'list-style-position':'outside',
                                'list-style-type':'square',
                                'color':'#ae5000',
                                'textAlign':'left',
                            }
                            
                        ),
                        ]
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Junior Trader",
                                style={
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Aug 2013 - Mar 2015"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#004640'
                            }
                        )
                        ],
                        style={
                        }
                    ),
                    dbc.Row(
                        [
                        html.Ul(
                            [
                            html.Li(
                                "Made independent trading decisions in a “swing trader” role alongside senior traders and position managers on various trading desks within the firm, including successfully running the firm’s coffee desk for a month during a manager transition "
                            ),
                            html.Li(
                                "Performed clerical work and manually executed futures orders across multiple desks, including Agriculture, Natural Gas and S&P 500, and completed intensive options theory and mock trading programs"
                            ),
                            ],
                            style={
                                'list-style-position':'outside',
                                'list-style-type':'square',
                                'color':'#ae5000',
                                'textAlign':'left',
                            }
                            
                        ),
                        ]
                    ),

                    ],
                    style={
                        'margin-left':'5%',
                        'margin-right':'5%',
                    }

                ),
                html.Hr(
                    style={
                        'border-width':'3px',
                        'width':'90%',
                        'color':'#ae5000',
                        'margin-left':'5%',
                        'margin-right':'5%',
                        'opacity':'unset'
                    }
                ),
                html.Div(
                    [
                    dbc.Row(
                        [
                        html.H4(
                            "KEY PROJECTS",
                            style={
                                'color':'#666600',
                                'margin-top':'10px',
                                'font-weight':'bold',
                            }
                        ),
                        html.Hr(
                            style={
                                'border-width':'2px',
                                'width':'86%',
                                'color':'#666600',
                                'opacity':'unset',
                                'margin-left':'7%',
                                'margin-right':'7%',
                            }
                        ),
                        dbc.Row(
                            [
                            html.H5(
                                "UCLA Master's Thesis: Building an Options Portfolio with Deep Learning",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            html.Ul(
                                [
                                html.Li(
                                    "Created a proof-of-concept Options Portfolio that takes daily long/short implied volatility positions in 315 underlying securities, leveraging the state-of-the-art Transformer Model as a foundation"
                                ),
                                html.Li(
                                    "Trained various end-to-end deep learning models that directly maximize the Sharpe Ratio, resulting in the Options Portfolio significantly outperforming all baselines and showing tremendous potential for use in an actual trading strategy"
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                }
                            ),
                            html.Hr(
                                style={
                                    'border-width':'2px',
                                    'width':'86%',
                                    'color':'#666600',
                                    'opacity':'unset',
                                    'margin-left':'7%',
                                    'margin-right':'7%',
                                }
                            ),
                             html.H5(
                                "Creating an Options Database and Live Volatility Surface App",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            html.Ul(
                                [
                                html.Li(
                                    "Developed an options database with real-time implied volatility surface visualizer, utilizing SQL, AWS RDS, and API application integration and wrote a script to automatically pull stock and options price data 3x daily and upload it to an AWS MySQL database. "
                                ),
                                html.Li(
                                    "Prioritized upload speed by adapting thread pooling for concurrent API calls and pandas for bulk SQL inserts and created a real-time implied volatility dashboard that displays a 3D visualization representing an asset's implied volatility surface "
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                }
                            ),
                            html.Hr(
                                style={
                                    'border-width':'2px',
                                    'width':'86%',
                                    'color':'#666600',
                                    'opacity':'unset',
                                    'margin-left':'7%',
                                    'margin-right':'7%',
                                }
                            ),
                             html.H5(
                                "IMDb Data Analysis",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            html.Ul(
                                [
                                html.Li(
                                    "Cleaned and engineered features for a dataset of over 5,000 films, including creating numerical variables for star actors, actresses, directors, and writers. "
                                ),
                                html.Li(
                                    "Trained a fully-connected neural network to predict inflation-adjusted box office profits and integrated it into a user-friendly app using the PyTorch framework and Plotly Dash."
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                }
                            ),
                           html.Hr(
                                style={
                                    'border-width':'2px',
                                    'width':'86%',
                                    'color':'#666600',
                                    'opacity':'unset',
                                    'margin-left':'7%',
                                    'margin-right':'7%',
                                }
                            ),
                             html.H5(
                                "Predictive Modeling with NFL Combine Data",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            html.Ul(
                                [
                                html.Li(
                                    "Demonstrated proficiency with scikit-learn for machine learning modeling, statsmodels for statistical analysis, and seaborn for data visualization, in a project focused on making NFL draft predictions using NFL Combine statistics"
                                ),
                                html.Li(
                                    "Collaborated with a partner to collect and clean data, and trained predictive models including logistic regression, random forest classifier, PCR and XGBoost to extract valuable insights, challenging conventional wisdom and suggesting other factors may play a significant role in predicting draft position"
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                }
                            ),
                            html.Hr(
                                style={
                                    'border-width':'2px',
                                    'width':'86%',
                                    'color':'#666600',
                                    'opacity':'unset',
                                    'margin-left':'7%',
                                    'margin-right':'7%',
                                }
                            ),
                             html.H5(
                                "Entity-Level Sentiment Analysis with Reddit Data",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold',
                                    'font-size':'18px'
                                }
                            ),
                            html.Ul(
                                [
                                html.Li(
                                    "Currently developing a sentiment analysis project that tracks individual player sentiment on the Los Angeles Lakers team throughout the 2022-23 season, using the reddit API to gather post and comment data from the Lakers subreddit"
                                ),
                                html.Li(
                                    "Plan to use spaCy library for entity recognition to isolate player names, before using the vaderSentiment library to analyze player sentiment at different time periods, with the ultimate goal of creating a user-friendly application for comparing player sentiment and statistics trends over time."
                                ),
                                ],
                                style={
                                    'list-style-position':'outside',
                                    'list-style-type':'square',
                                    'color':'#ae5000',
                                    'textAlign':'left',
                                }
                            ),

                            ],
                        ),  
                        ],
                    ),
                    ],
                    style={
                        'margin-left':'5%',
                        'margin-right':'5%',
                    }
                ),
                html.Hr(
                    style={
                        'border-width':'3px',
                        'width':'90%',
                        'color':'#ae5000',
                        'margin-left':'5%',
                        'margin-right':'5%',
                        'opacity':'unset'
                    }
                ),
                html.Div(
                    [
                    dbc.Row(
                        html.H4(
                            "EDUCATION & CERTIFICATIONS",
                            style={
                                'color':'#666600',
                                'font-weight':'bold',
                                'margin-top':'10px',
                                'margin-bottom':'-10px'
                            }
                        )
                    ),
                    html.Hr(
                        style={
                            'border-width':'2px',
                            'width':'86%',
                            'color':'#666600',
                            'opacity':'unset',
                            'margin-left':'7%',
                            'margin-right':'7%',
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "The University of California, Los Angeles",
                                style={
                                    'font-weight':'bold'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640',
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "GPA: 4.0/4.0"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#ae5000',
                                'font-weight':'bold'
                            }

                        )
                        ],
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.P(
                                "Master of Applied Statistics",
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#ae5000',
                                'font-size':'16px',
                                'font-style':'italic'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Expected June 2023"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#ae5000',
                            }

                        )
                        ],
                        style={
                            'margin-top':'-15px',
                            'margin-bottom':'-10px'
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Boston College CSOM Honors Program",
                                style={
                                    'font-weight':'bold'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640',
                                'font-weight':'bold'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "GPA: 3.6/4.0"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#ae5000',
                                'font-weight':'bold'
                            }

                        )
                        ],
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.P(
                                "B.S. Management; Concentrations in Finance, Accounting; Minor in Mathematics ",
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#ae5000',
                                'font-size':'16px',
                                'font-style':'italic'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "2013"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#ae5000'
                            }

                        )
                        ],
                        style={
                            'margin-top':'-15px',
                            'margin-bottom':'-10px'
                        }
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "CFA Charterholder",
                                style={
                                    'font-weight':'bold'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Aug 2017"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#ae5000'
                            }

                        )
                        ],
                    ),
                    dbc.Row(
                        [
                        dbc.Col(
                            html.H5(
                                "Machine Learning Scientist with Python: DataCamp",
                                style={
                                    'font-weight':'bold'
                                }
                            ),
                            style={
                                'textAlign':'left',
                                'color':'#004640'
                            }
                        ),
                        dbc.Col(
                            html.P(
                                "Mar 2023"
                            ),
                            style={
                                'textAlign':'right',
                                'color':'#ae5000'
                            }

                        )
                        ],
                    ),
                    ],
                    style={
                        'margin-left':'5%',
                        'margin-right':'5%'
                    }
                ),
                html.Hr(
                    style={
                        'border-width':'3px',
                        'width':'90%',
                        'color':'#ae5000',
                        'margin-left':'5%',
                        'margin-right':'5%',
                        'opacity':'unset'
                    }
                ),
                dbc.Row(
                    style={
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
    ],
)
            