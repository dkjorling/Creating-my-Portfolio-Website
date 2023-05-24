import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

#my imports
from dash_helpers import page_top, page_bottom
####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/website')


load_figure_template('FLATLY')

layout = html.Div(
    children=[
        page_top(),
        html.Div(
            children=[
                dbc.Row(
                    [
                    dbc.Col(
                        html.H2(
                            "Creating my Portfolio Website",
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
                                    "Code",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='https://github.com/dkjorling/Creating-my-Portfolio-Website',
                            style={
                                'padding':'0px 15px 0px 30px',
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
                            "I built my portfolio website using Dash, a Python framework for building web applications. The website showcases my proficiency in data analysis, statistical modeling, and data visualization through a collection of projects I have completed. The website features a clean and intuitive design, with easy navigation to each project's page. On each project's page, visitors can view a brief description of the project, as well as data visualizations and dashboards created using Plotly.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "To ensure the website's scalability and reliability, I deployed it to AWS using Elastic Beanstalk, a fully managed service that handles the deployment, scaling, and monitoring of web applications. Visitors can access the website from anywhere with an internet connection, and the website's performance is optimized for a smooth user experience.",
                            style={
                                'font-size':'16px',
                                'color':'#666600'
                            }
                        ),
                        html.P(
                            "Overall, this project demonstrates my ability to effectively communicate my skills and accomplishments through a professional and user-friendly website. It also showcases my proficiency in utilizing various tools and technologies to create a seamless and engaging online experience for visitors. ",
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
                                "Web Design with Dash: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Utilize Dash to design entirety of website and embed projects and dashboards",
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
                                "Deployment with AWS EB: ",
                                style={
                                    'color':'#004640',
                                    'font-weight':'bold'
                                },
                            ),
                            "Deploy website to AWS server using Elastic Beanstalk",
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
                            "Dash, AWS Elastic Beanstalk",
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
