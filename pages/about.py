import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output, register_page, get_asset_url
from dash_bootstrap_templates import load_figure_template

# my impots
from dash_helpers import page_top, page_bottom


####################################################################################
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/about')


load_figure_template('FLATLY')

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
                            "ABOUT",
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
                    [
                    dbc.Col(
                        dbc.Stack(
                            [
                            html.Div(
                                children=[
                                    html.Img(
                                        src=r'assets/profile.jpg',
                                        style={
                                            'padding':'3px',
                                            'height':'75%',
                                            'width':'75%',
                                            'border':'2px solid burlywood',
                                            'margin':'15px 0px 15px 0px'
                                        }
                                    ),
                                    html.H4(
                                        "Areas of Interest and Expertise",
                                        style={
                                            'font-size':'24px',
                                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                            'font-weight':'bold',
                                            'textAlign':'left',
                                            'color':'#666600',
                                            'padding':'15px 0px 0px 0px'
                                        }
                                    ),
                                    html.H4(
                                        [
                                        html.Li(
                                            "Deep Learning in Finance"
                                        ),
                                        html.Li(
                                            "Machine Learning in Sports Analytics"
                                        ),
                                        html.Li(
                                            "Social Media NLP"
                                        ),
                                         html.Li(
                                            "Derivatives Trading"
                                        ),
                                        ],
                                        style={
                                            'color':'#ae5000',
                                            'font-size':'20px',
                                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                            'textAlign':'left',
                                            'padding':'0px',
                                            'list-style-type':'square'
                                        }
                                    ),
                                    html.H4(
                                        "Personal",
                                        style={
                                            'font-size':'24px',
                                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                            'font-weight':'bold',
                                            'textAlign':'left',
                                            'color':'#666600',
                                            'padding':'15px 0px 0px 0px'
                                        }
                                    ),
                                    html.P(
                                        "In my free time you can find me taking a long run on the strand, snowboarding at Mammoth Mountain, exploring new destinations around the globe, or cheering on my beloved Bengals and Lakers!",
                                        style={
                                            'color':'#ae5000',
                                            'font-size':'18px',
                                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                            'textAlign':'left',
                                            'padding':'0px'
                                        }
                                    )
                                ]
                            ),

                        ]
                        ),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'0px 15px 15px 45px',
                            'width':'20%',
                            'textAlign':'center'
                        }
                    ),
                    dbc.Col(
                        dbc.Stack(
                            [
                            html.H4(
                                "Bio",
                                style={
                                    'font-size':'24px',
                                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                    'font-weight':'bold',
                                    'textAlign':'left',
                                    'color':'#666600',
                                    'padding':'15px 0px 0px 0px'
                                }
                            ),
                            html.P(
                                "Throughout my educational and professional journey, I have honed my exceptional problem-solving and critical thinking skills, utilizing data-driven insights to optimize decision making and deliver outstanding results. After studying Finance, Accounting and Mathematics at Boston College, I spent nearly ten years in derivatives trading, the last four of which were in the role of Portfolio Manager where I lead a team that generated over $5 million in trading profit annually.",
                                style={
                                    'color':'#ae5000',
                                    'font-size':'17px',
                                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            html.P(
                                "Driven by a desire to accentuate my analytical and coding skills and move back home to Los Angeles, I decided to a pursue a Master’s of Applied Statistics degree from UCLA and am on track to graduate in June 2023 with a 4.0 GPA. The cornerstone of my graduate education is my Master’s thesis, titled “Building an Options Portfolio”, where I utilize state of the art deep learning models and my derivatives background to develop a novel proof-of-concept options portfolio (see Portfolio for details). I have also earned CFA certification and Machine Learning Scientist certification from DataCamp, showcasing my dedication to an ongoing educational pursuit. ",
                                style={
                                    'color':'#ae5000',
                                    'font-size':'17px',
                                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            ),
                            html.P(
                                "Whether I am analyzing complex financial data, leveraging ML algorithms to identify new opportunities, or designing stunning data visualization dashboards, I am committed to delivering excellence and am excited for my next career opportunity. Please enjoy my portfolio projects and reach out with any inquiries. ",
                                style={
                                    'color':'#ae5000',
                                    'font-size':'17px',
                                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                                    'textAlign':'left',
                                    'padding':'0px'
                                   }
                            )


                        ]
                        ),
                        style={
                            'background-color':'#faf0e6',
                            'margin':'0px 45px 15px 15px',
                            'width':'80%',
                            'textAlign':'center'
                        }
                    ),
                    ]
                ),

                html.Div(
                    children=[
                        html.A(
                            html.Button(
                                    "Detailed C.V.",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/cv',
                            style={
                                'padding':'0px 15px 0px 0px',
                                'textAlign':'center'
                            }
                        ),
                        html.A(
                            html.Button(
                                    "Resumé",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/assets/resume.pdf',
                            style={
                                'padding':'0px 15px 0px 15px',
                                'textAlign':'center'
                            }
                        ),
                        
                        html.A(
                            html.Button(
                                    "Contact",
                                    style={
                                        'color':'white',
                                        'font-size':'20px',
                                        'background-color':'#666600',
                                    },
                            ),
                            href='/contact',
                            style={
                                'padding':'0px 0px 0px 15px',
                                'textAlign':'center'
                            }
                        ),
                    ],
                    style={
                        'padding':'15px 0px 15px 0px',
                        'textAlign':'center',
                        'padding':'0px 0px 300px 0px',
                    }
                ),

            
            ],
            style={
                'background-color':'seashell'
            }
        ),
        page_bottom(),
     ]
)
