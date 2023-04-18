import dash_bootstrap_components as dbc
from dash import html, register_page
from dash_bootstrap_templates import load_figure_template

from dash_helpers import dashboard_navbar2, page_bottom

####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/optionsport/dashboard/documentation')

load_figure_template('FLATLY')

### Begin Page Layout ###
layout = html.Div(
            children=[
                dashboard_navbar2(
                                'optionsport',
                                'seagreen',
                                'white',
                                'seagreen'
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            'Options Portfolio Dashboard Documentation',
                            style={
                                "color": "white",
                                'padding':'15px 0px 0px 15px',
                                'font-weight':'bold'
                            }
                        ),
                        style={
                            'background-color':'darkslategray',
                            'border-top':'3px solid seagreen'
                            }
                        ),
                    ]
                ),
    
                dbc.Row(
                    [
                    html.H4(
                        'General Dashboard Overview',
                        style={
                            'color':'seagreen',
                            'font-weight':'bold',
                            'padding':'15px 0px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.P(
                        "This dashboard contains analysis plots related to both model performance and underlying asset implied volatility through time. Each model-driven plot allows users to compare various performance metrics between the Attention Transformer, LSTM, GRU and equal-weighted portfolios. The asset IV plots enable users to compare implied volatility correlations between any of the 315 stocks and ETFs used in the study. Finally, note that implied volatility in the context of this study references the implied volatility of the 60-day until expiration at-the-money straddle.",
                        style={
                            'color':'black'
                        }
                        ),
                    html.Br(),
                    ],
                    style={
                        'background-color':'whitesmoke',
                        'margin':'15px'
                    }
                ),
    
                dbc.Row(
                    [
                    html.H4(
                        'Model Metrics',
                        style={
                            'color':'seagreen',
                            'font-weight':'bold',
                            'padding':'15px 0px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.H5(
                        'Rolling Parameters by Model',
                        style={
                            'color':'darkslategray'
                        }
                    ),
                    html.P(
                        'Adjustable Parameters: Performance Metric, Date Range',
                        style={
                            'font-style':'italic',
                            'color':'seagreen'
                        }
                    ),
                    html.Ul(
                        html.Li(
                            'Show rolling annualized performance metrics for each model, including Sharpe Ratio, Sortino Ratio and Calmar Ratio ',
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.H5(
                        'Monthly Returns Heatmap',
                        style={
                            'color':'darkslategray'
                        }
                    ),
                    html.P(
                        'Adjustable Parameters: Model',
                        style={
                            'font-style':'italic',
                            'color':'seagreen'
                        }
                    ),
                    html.Ul(
                        html.Li(
                            'Display monthly percent returns for the selected model portfolio over the span of the study'
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.Br(),
                    ],
                    style={
                        'background-color':'whitesmoke',
                        'margin':'15px',
                    }
                ),
                
                
                dbc.Row(
                    [
                    html.H4(
                        'Volatility Exposure and Long/Short IV Levels',
                        style={
                            'color':'seagreen',
                            'font-weight':'bold',
                            'padding':'15px 0px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.P(
                        'Adjustable Parameters: Model, Rolling Window Type, Date Range',
                        style={
                            'font-style':'italic',
                            'color':'seagreen'
                        }
                    ),
                    html.Ul(
                        [
                        html.Li(
                            'Dual y-axis plot displaying both net rolling implied volatility exposure of each model over time [left axis] and mean implied volatility of all assets [right axis]',
                        ),
                        html.Li(
                            'Net IV exposure is defined as: |Portfolio Weights of all Long Positions| - |Portfolio Weights of all Short Positions|',
                        ),
                        html.Li(
                            'Mean implied volatility is segregated, as mean IV of portfolio long positions are represented by a green line and mean IV of portfolio short positions are represented by a red line.'
                        ),
                        html.Li(
                            'The horizontal orange dotted line represents the average net IV exposure for the given model portfolio. ',
                        ),
                        ],
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.Br(),
                    ],
                    style={
                        'background-color':'whitesmoke',
                        'margin':'15px',
                    }
                ),
                
                dbc.Row(
                    [
                    html.H4(
                        'Asset IV over time and Correlations',
                        style={
                            'color':'seagreen',
                            'font-weight':'bold',
                            'padding':'15px 0px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.Ul(
                        html.Li(
                            'These two plots are meant to be used in conjunction to identify trends in implied volatility and analyze inter-asset IV correlations.'
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.H5(
                        'Rolling Implied Volatility',
                        style={
                            'color':'darkslategray'
                        }
                    ),
                    html.P(
                        'Adjustable Parameters: Assets, Rolling Window Type, Years (slider on bottom of panel)',
                        style={
                            'font-stye':'italic',
                            'color':'seagreen'
                        }
                        ),
                    html.Ul(
                        html.Li(
                            'Display rolling average implied volatility for selected assets over a specified timeframe'
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 45px 5px 15px'
                        }
                    ),
                    
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.H5(
                        'Implied Volatility Correlation Heatmap',
                        style={
                            'color':'darkslategray'
                        }
                    ),
                    html.P(
                        'Adjustable Parameters: Assets, Years (slider on bottom of panel)',
                        style={
                            'font-stye':'italic',
                            'color':'seagreen'
                        }
                    ),
                    
                    html.Ul(
                        html.Li(
                            'Show volatility correlations as a heatmap for specified assets and timeframe'
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.Br(),
                    ],
                    style={
                        'background-color':'whitesmoke',
                        'margin':'15px',
                    }
                ),
                
                dbc.Row(
                    [
                    html.H4(
                        'Model Comparison',
                        style={
                            'color':'seagreen',
                            'font-weight':'bold',
                            'padding':'15px 0px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.H5(
                        'Portfolio Values',
                        style={
                            'color':'darkslategray'
                        }
                    ),
                    html.P(
                        'Adjustable Parameters: Date Range',
                        style={
                            'font-style':'italic',
                            'color':'seagreen'
                        }
                    ),
                    html.Ul(
                        html.Li(
                            'Display cumulative portfolio values through time for each model with beginning values equivalent to 1.0'
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.H5(
                        'Model Annual Returns',
                        style={
                            'color':'darkslategray'
                        }
                    ),
                    html.P(
                        'Adjustable Parameters: Model, Years (Slider beneath plots)',
                        style={
                            'font-style':'italic',
                            'color':'seagreen'
                        }
                    ),
                    html.Ul(
                        html.Li(
                            'Show annual returns for the selected model portfolio and timeframe'
                        ),
                        style={
                            'color':'black',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px'
                        }
                    ),
                    html.Br(),
                    ],
                    style={
                        'background-color':'whitesmoke',
                        'margin':'15px',
                    }
                ),
                
                dbc.Row(
                    [
                    html.H4(
                        'Plot Interactivity',
                        style={
                            'color':'seagreen',
                            'font-weight':'bold',
                            'padding':'15px 0px 0px 15px'
                        }
                    ),
                    html.Hr(
                        style={
                                'color':'seagreen',
                                'width':'95%',
                                'margin':'0px 0px 5px 15px',
                                'border-width': '2px'
                            }
                    ),
                    html.Ul(
                        [
                        html.Li(
                            'Hoverability: Hovering over plots displays more granular detail dependent on the plot type'
                        ),
                        html.Li(
                            'Zoomability: Above each plot exists a "+" and "-" allowing users to zoom in and out respectively'
                        ),
                        html.Li(
                            'Display Options: Line plots have toggle options available allowing users to determine what data is displayed'
                        ),
                        ],
                        style={
                            'color':'darkslategray',
                            'list-style-type':'square',
                            'list-style-position':'outside',
                            'margin':'0px 0px 5px 15px',
                            'padding':'0px 45px 0px 15px',
                            'font-size':'20px'
                        }
                    ),
                    html.Br(),
                    ],
                    style={
                        'background-color':'whitesmoke',
                        'margin':'15px',
                    }
                ), 
                dbc.Row(
                    style={
                        'background-color':'seagreen',
                        'height':'300px',   
                        'width':'110%',
                        'border-top':'10px solid darkslategray'
                    }
                ),  
                page_bottom(col1='seagreen', col2='seagreen', col3='white'),
                ],
                 style={
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    'background-color':'darkslategray'
                }
            )
 ## final container brackets do not move
                      

        
        
        
        
        
        
        
        
        
        
    
