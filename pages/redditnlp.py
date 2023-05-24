import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/redditnlp')


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
                            "Entity-Level Sentiment Analysis with Reddit Data",
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
                            href='/redditnlp/dashboard',
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
                            href='https://github.com/dkjorling/Entity-Level-Sentiment-Analysis-with-Reddit-Data',
                            style={
                                'padding':'15px 0px 15px 0px',
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
                            href='/assets/reddit.pdf',
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
                            "This project focuses on the extraction of entity-level sentiment from users of the r/Lakers subreddit towards each player on the Los Angeles Lakers team throughout the entire 2022-23 NBA regular season. By employing advanced sentiment analysis techniques, the project aims to gain deeper insights into the sentiments expressed towards individual players and analyze the data in various ways.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "Traditionally, unsupervised sentiment analysis involves using a pre-trained model to assign sentiment to a text input, such as posts or comments. Entity-level sentiment analysis takes this a step further by obtaining sentiment specifically related to each entity mentioned in the text. The goal of this project is to extract the sentiment associated with every player on the team from each post or comment. Entity-level sentiment analysis enables the extraction of more interesting insights, especially when combined with additional data such as player statistics. Key information sought from this analysis includes identifying the most and least-liked players during different periods of the year, understanding the close associations between players, and examining the alignment of players' sentiment with team and individual performance.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "To overcome the limitations of the Reddit API, which only allows access to the latest 1,000 posts, the project utilized the less restrictive PushShift API. This enabled the collection of a substantial dataset consisting of 11,000 posts and 147,000 comments, spanning the entirety of the NBA season. The collected data underwent basic cleaning procedures, including lowercasing, special character removal, and hyperlink elimination. Entity recognition was a critical step in this project, accomplished through a customized approach that combined domain knowledge and regex patterns. This approach ensured accurate identification of player mentions in the data.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "The Vader Sentiment library was employed for the task of sentiment analysis and enhanced to provide precise sentiment analysis for the desired entities. Incremental adjustments made to the sentiment lexicon, include nickname adjustments, emoji-lexicon adjustments, basketball-related lexicon adjustments, and part-of-speech resolving. These modifications were implemented to improve the accuracy and relevance of the sentiment analysis results. To comprehensively extract player mentions, co-reference resolving techniques were implemented. This process leveraged reddit’s hierarchical structure to identify all indirect mentions of a player by combining parent-child text and replacing pronouns with named entities. Additionally, sentence tokenization was implemented to isolate sentences specific to each entity for sentiment analysis, thereby enhancing the accuracy of the results. ",
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
                    ),
                ]
                ),
                dbc.Row(
                    [
                    dbc.Col(
                        [
                        html.Div(
                            [
                            html.Img(
                                src='assets/psent.png',
                                style={
                                    'font-size':'22px',
                                    'border':'#ae5000 solid 2px',
                                    'margin':'15px',
                                    'width':'40%',
                                }
                            ),
                            ],
                            style={
                                'textAlign':'center'
                            }
                        ),
                        html.P(
                            "Sentiment scores are calculated by subtracting the proportion of negative posts/comments from the proportion of positive posts/comments for each individual player. It is unsurprising that the two highest sentiment scores belong to players who were acquired mid-season, given the Lakers' below-average excellent finish.  While star players Lebron James and Anthony Davis accounted for approximately 40% of total player mentions, they had two of the lowest sentiment scores on the entire team. Fans were clearly not impressed with the team’s mediocrity for a majority of the season and seemingly put a majority of the blame on its best players. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "Young, new players on the other hand had generally higher sentiment ratings than their more established counterparts. This could potentially be linked to excitement over a new, unknown player or enthusiasm about a young player’s potential going forward. Russell Westbrook, acquired the previous season, had a low sentiment score, likely due to the large drop-off in team performance coinciding with his arrival.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.Div(
                            [
                            html.Img(
                                src='assets/psent_ntrg.png',
                                style={
                                    'font-size':'22px',
                                    'border':'#ae5000 solid 2px',
                                    'margin':'15px',
                                    'display':'inline-block',
                                    'width':'38%'
                                }
                            ),
                            html.Img(
                                src='assets/psent_wpct.png',
                                style={
                                    'font-size':'22px',
                                    'border':'#ae5000 solid 2px',
                                    'margin':'15px',
                                    'display':'inline-block',
                                    'width':'38%'
                                }
                            ),
                            ],
                            style={
                                'textAlign':'center'
                            }
                        ),
                        
                        html.P(
                            "Analyzing on-court statistics vs player sentiment is another way to learn more about how fans think and whose sentiment is most and least sensitive to both individual and team-based performance. The two plots above display player sentiment correlation with Net Rating, a comprehensive individual statistic, and team winning percentage. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.Div(
                            [
                            html.Img(
                                src='assets/beas_tbj.png',
                                style={
                                    'font-size':'22px',
                                    'border':'#ae5000 solid 2px',
                                    'margin':'15px',
                                    'width':'70%',
                                }
                            ),
                            ],
                            style={
                                'textAlign':'center'
                            }
                        ),
                        html.P(
                            "Malik Beasley, a solid yet unspectacular role player, has the highest sentiment-Net Rating correlation on the team. This could potentially be attributed to his high-variance play style as a high-volume, somewhat inconsistent three-point shooter. Additionally, his status as a new player acquired midseason likely contributes to this notion. It is not surprising to see fan sentiment toward star player LeBron James’s being highly correlated with his on-court performance, but it is notable that the other team star, Anthony Davis, is more middle-of-the-pack in terms of sentiment correlation. On the other hand, players with negative correlation are mainly young players with future potential and generally high overall sentiment scores. The figure above highlights the stark differences between Malik Beasley and Troy Brown Jr. in terms of sentiment-net rating correlation.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.Div(
                            [
                            html.Img(
                                src='assets/bron_dlo.png',
                                style={
                                    'font-size':'22px',
                                    'border':'#ae5000 solid 2px',
                                    'margin':'15px',
                                    'width':'70%',
                                }
                            ),
                            ],
                            style={
                                'textAlign':'center'
                            }
                        ),
                        html.P(
                            "At first glance, the team win percentage plot appears to be evenly dispersed, with a slight negative skew.  It is interesting to note that more players' sentiment is negatively correlated with team winning percentage than positively correlated. Sentiments towards the team's top players are amongst the most positively correlated with team winning percentage. Taken together, this indicates that sentiment towards star players is highly dependent on team performance, while sentiment towards role players is much more related to individual performance. The figure above displays two ends of this spectrum: Lebron James and D’Angelo Russell. ",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "The findings of this project emphasize the power of player-level sentiment analysis in uncovering meaningful patterns in fan behavior, which can be instrumental in shaping effective marketing strategies. Moreover, entity-level sentiment analysis has broad applications beyond the realm of basketball, such as analyzing sentiment towards specific stocks on social media or gauging public sentiment towards potential Presidential candidates. The versatility of this analysis approach makes it a valuable tool in diverse domains and opens up countless opportunities for its application.",
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
                                "Web Scraping with requests: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Scrape entire Lakers reddit history and player statistics for the 2022-23 season",
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
                                "Entity Recognition: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Leverage domain knowledge and regex expertise to accurately and comprehensively extract player entities",
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
                                "Advanced NLP Techniques with SpaCy: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Utilize part-of-speech recognition to resolve dual-meaning terms and co-reference resolution to extract additional entity references. ",
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
                                "Sentiment Analysis with vaderSentiment: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Enhance base sentiment by creating a basketball-lexicon with emojis and incorporating sentence tokenization to better isolate entity-level sentiment",
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
                            "requests, spaCy, vaderSentiment, nltk, pandas, Dash",
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
                'background-color':'seashell',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        ),
        page_bottom(),
    ]
)


