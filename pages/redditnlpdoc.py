import dash_bootstrap_components as dbc
from dash import html, register_page
from dash_bootstrap_templates import load_figure_template

# my imports
from components.helpers import page_bottom


################################################
colors = ['#552583', '#FDB927', 'white', '#405ED7', "#FDB927"]

### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/redditnlp/dashboard/documentation')



load_figure_template('FLATLY')

layout = html.Div(
    children=[
        dbc.Row(
            [
            dbc.Col(
                width={'size':8}
            ),
            dbc.Col(
                [
                html.Div(
                    [
                    html.A(
                        "Dashboard",
                        href="/redditnlp/dashboard/",
                        style={
                            'color': colors[0],
                            'font-size':'18px',
                            'margin':'0px 0px 0px 0px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),
                    html.A(
                        "Overview",
                        href="/redditnlp",
                        style={
                            'color': colors[0],
                            'font-size':'18px',
                            'margin':'0px 0px 0px 15px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),

                    html.A(
                        "Portfolio",
                        href="/portfolio",
                        style={
                            'color': colors[0],
                            'font-size':'18px',
                            'margin':'0px 0px 0px 15px',
                            'font-weight':'bold',
                            'display':'inline-block',
                        }
                    ),
                    ]
                )
                ],
                width={'size':4},
            ),
            ],
            style={
                'background-color':colors[1],
                'width':'110%',
                'margin-botton':'5px',
            }
        ),
        dbc.Row(
            [
            html.H3(
            'Reddit NLP Dashboard Documentation',
            style={
                'color':colors[1],
            }
            ),
            ],
            style={
                'margin':'15px 0px 0px 30px',
                'font-weight':'bold'
            }
        ),
        
        dbc.Row(
            [
            html.H5(
                'Navigation Bar',
                style={
                    'color':'white'
                }
            ),
            html.P(
                "The dropdown menus in the top-line navigation bar control most of the content displayed in the dashboard. “Select Entity” defaults to entire team sentiment while “Select Date” defaults to the last day of the season, April 10, 2023. Additional entity options include Jeanie Buss, the team owner, Rob Pelinka, the general manager, and Darvin Ham, the coach. Sentiment stats are displayed throughout the dashboard for the selected entity up to the selected date, allowing for users to observe how sentiment has changed through time. Clicking “Players” takes users to the players page where a similar dropdown exists to choose a desired player and date for sentiment to be viewed. ",
                style={
                    'color':colors[1]
                }
            )
            ],
            style={
                'margin':'0px 0px 0px 30px'
            }
        ),
        dbc.Row(
            [
            html.H5(
                'Sentiment Stats',
                style={
                    'color':'white'
                }
            ),
            html.P(
                "Sentiment stats are displayed for year-to-date (YTD) sentiment, including a pie chart with negative, positive and neutral sentiment proportions. The sentiment displayed is calculated simply by subtracting the negative sentiment proportion from the positive sentiment proportion. Additionally, sentiment in the prior 20-day period up to the selected date is displayed along with a trend comparing YTD to the past 20 days. The players page has an additional feature comparing the selected player’s sentiment stats to average player sentiment. ",
                style={
                    'color':colors[1]
                }
            )
            ],
            style={
                'margin':'0px 0px 0px 30px'
            }
        ),
        dbc.Row(
            [
            html.H5(
                'Statistics, Term Frequencies & Player Associations',
                style={
                    'color':'white'
                }
            ),
            html.P(
                "The statistics panel allows users to view year-to-date team or player stats in per-game, per-100 possessions, cumulative or per-36 minutes (players only) terms. The Sentiment Type dropdown controls the top-10 frequency terms and top-10 frequency emojis plots, allowing users to view top terms and emojis for total, positive-only or negative-only mentions. ",
                style={
                    'color':colors[1]
                }
            ),
            html.P(
                "The team dashboard contains a Relative Player Associations plot displaying mean-adjusted percentage mentions for each player pairing. For example, the row named “ad” measures relative player associations with Anthony Davis, where on average, other players are mentioned in 18.4% of his posts/comments. Subtracting out this mean across all players results in the displayed values, showing that Lebron is mentioned in 16.6% greater-than-average AD mentions (35% total), and Austin Reaves is mentioned in 12.6% less-than-average AD mentions (5.8% total). ",
                style={
                    'color':colors[1]
                }
            )
            ],
            style={
                'margin':'0px 0px 0px 30px'
            }
        ),
        dbc.Row(
            [
            html.H5(
                'Sentiment Plots',
                style={
                    'color':'white'
                }
            ),
            html.P(
                "The last two panels contain separate sentiment plots. The first displays positive and negative mentions in 3-day samples throughout the course of the season, in addition to the sentiment score. The final panel displays rolling 20-day sentiment score vs rolling 20-day user-selected statistics throughout the course of the season.  ",
                style={
                    'color':colors[1]
                }
            )
            ],
            style={
                'margin':'0px 0px 0px 30px'
            }
        ),
        dbc.Row(
            style={
                'height':'300px',   

            }
        ),
        page_bottom(col1=colors[1], col2=colors[0], col3=colors[0])
    ],
    style={
        'background-color':colors[0],
        'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
    }
)