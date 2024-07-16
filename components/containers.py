import dash_bootstrap_components as dbc
import json
from components.helpers import (
    proj_image, get_buttons, Navbar, get_bottom_nav_item, get_project_title_container, get_proj_pages_buttons,
    get_all_project_skills_container, get_all_project_content_section_containers, get_page_bottom_container,
    get_project_content_section_container, get_about_button_container, get_about_header, get_about_left_container,
    get_about_right_container, get_contact_top_containers, get_contact_bottom_container, get_home_top_container,
    get_home_bottom_container
)
from dash import html

################################# Load Data #################################
# Load portfolio page config
with open("config/portfolio_page_config.json", "r") as f:
    portfolio_page_config = json.load(f)

# Load portfolio page config
with open("config/pages_config.json", "r") as f:
    pages_config = json.load(f)

# Load other page config
with open("config/other_pages_config.json", "r") as f:
    other_config = json.load(f)
################################# General Containers #################################
def page_top():
    """
    This function provides a container featuring the Navbar on the top of the website

    Returns
    -------
    
    """
    top = dbc.Row(
            [
            Navbar()
            ]
        )
    return top

def page_bottom(col1='#004640', col2='#ae5000', col3='white'):
    bottom = dbc.Stack(
        [
        dbc.Col(
                children=[
                    get_bottom_nav_item(
                        text="Link to my LinkedIn",
                        href="https://www.linkedin.com/in/dylan-jorling-cfa-75729045/",
                        im_path="li.png"
                        ),
                    get_bottom_nav_item(
                        text="Link to my GitHub",
                        href="https://github.com/dkjorling",
                        im_path="gh.png"
                        ),
                ],
                style={
                    'background-color':col1,
                    'textAlign':'center',
                }
            ),
            dbc.Col(
                html.H5(
                    'Copyright © 2023 | Dylan Jorling',
                    style={
                        'color': col3,
                        'padding':'0px 0px',
                        'font-size':'12px',
                    }
                ),
                style={
                'background-color':col1,
                'textAlign':'center',
                }
            ),
            ],
            style={
                'background-color':col1,
                'textAlign':'center',
                'position':'fixed',
                'bottom':'0',
                'width':'100%',
                'border-top':'3px solid {}'.format(col2)
            },
        )
    return bottom

################################# Containers for Portfolio Page #################################
def create_project_rows(project_names):
    """
    Iterate through project names and return two projects per row.

    Parameters
    ----------
    project_names : list of str
        Names of the projects that correspond to portfolio_page_config file keys
    
    Returns
    -------
    dbc object
        returns dbc object representing rows of project containers
    """
    rows = []
    for i in range(0, len(project_names), 2):
        left_project = project_names[i]
        right_project = project_names[i + 1] if i + 1 < len(project_names) else None

        row = dbc.Row(
            [
                project_container(left_project, side='left'),
                project_container(right_project, side='right') if right_project else project_container(page_key=None, side='right')
            ],
            style={
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif'
            }
        )
        rows.append(row)
    return rows
def project_container(page_key, side='left'):
    """
    Object containing info for a project

    Parameters
    ----------
    page_key : str
        String indicating the key to pull data for configuration
    
    Returns
    -------
    dbc object
        returns dbc object representing a dbc column containing layout for a project
    """
    # Define margin based on page size
    if side == 'left':
        margin = '15px 15px 15px 40px'
    elif side == 'right':
        margin = '15px 40px 15px 15px'
    else:
        raise ValueError("Side ust be either 'left' or 'right'!")

    if page_key is None:
        return dbc.Col(
            style={
            'background-color':'#faf0e6',
            'margin':margin,
            'width':'50%',
            'border':'1px solid #666600',
            'textAlign':'center'
        }
        )

    # Initiate Container
    container = dbc.Col(
        dbc.Stack([
            html.H4(
                # Get project title from config
                portfolio_page_config[page_key]['title'],
                style={
                    'color':'#ae5000',
                    'padding':'10px 10px 0px 10px',
                    'font-size':'18px',
                    'textAlign':'center',
                    'font-weight':'bold'
                }
            ),
            html.P(
                # Get project summary from config
                portfolio_page_config[page_key]['summary'],
                style={
                    'color':'#666600',
                    'font-size':'12px',
                    'textAlign':'left',
                    'padding':'0px'
                    }
            ),
            # Get photo path from config
            proj_image(portfolio_page_config[page_key]['photo_path'], height='84%', width='84%'),
            
            html.Div([
                html.Span(
                    # Get Broad Skill Subject from config
                    f"SKILLS [" + ", ".join(portfolio_page_config[page_key]['skills1']) + "]: ",
                    style={
                        'color':'#004640'
                    },
                ),
                # Get Detailed Skills from config
                ", ".join(portfolio_page_config[page_key]['skills2']),
                ],
                style={
                    'color':'#ae5000',
                    'font-size':'12px',
                    'textAlign':'center',
                    'padding':'5px'
                }
            ),
            # Get properly formatted buttons
            
            get_buttons(portfolio_page_config[page_key]['buttons']),
            
            
        ]),
        style={
            'background-color':'#faf0e6',
            'margin':margin,
            'width':'50%',
            'border':'1px solid #666600',
            'textAlign':'center'
        }
    )
    return container

################################# Containers for Individual Project Pages #################################
def get_project_page_layout(project, pages_config):
    """
    Parameters
    ----------
    project: str
        String representing project name in config file
    pages_config : dict
        Project configuration dictionary

    Returns
    -------
    dash.html.Div
        dash object representing project page layout
    """
    layout = html.Div(
        children=[
            page_top(),
            html.Div(
                children=[
                    get_project_title_container(pages_config[project]['title']),
                    get_proj_pages_buttons(pages_config[project]['buttons']),
                    *get_all_project_content_section_containers(pages_config[project]['content'], project),
                    get_all_project_skills_container(pages_config[project]['skills'], project),
                    get_page_bottom_container(),
                ],
                style={'background-color':'seashell'}
            ),
            page_bottom(),
        ],
        style={'font-family': 'Montserrat, Helvetica, Arial, sans-serif'}
    )
    return layout

################################# Containers for Other Pages #################################

def get_home_layout_container(other_config):
    """
    Returns container for the 'Home' Page
    """
    layout = html.Div(
        children=[
            page_top(),
            html.Div(
                children=[
                    *get_home_top_container(other_config),
                    *get_home_bottom_container()
                ],
                 style={
                'background-color':'seashell',
                'width':'100%'
                }
            ),
            page_bottom()
        ]
    )
    return layout

def get_about_container_layout(other_config):
    """
    Returns container for the 'About' Page
    """
    layout = html.Div(
        children=[
            page_top(),
            html.Div(
                [
                    html.Br(),
                    get_about_header(),
                    dbc.Row(
                        [
                            get_about_left_container(other_config['about']['content']),
                            get_about_right_container(other_config['about']['content'][2]),
                        ]
                    ),
                    get_about_button_container(other_config['about']['buttons'])
                ],
                 style={'background-color':'seashell'}
            ),
            page_bottom()
        ],
        style={'font-family': 'Montserrat, Helvetica, Arial, sans-serif'}
    )
    return layout

def get_contact_layout(other_config):
    """
    Get contact page layout
    """
    # Get individual content container rows
    contact_row1, contact_row2 = get_contact_top_containers(other_config)
    contact_row3 = get_contact_bottom_container(other_config)

    layout = html.Div(
        children=[
            page_top(),
            html.Div(
                children=[
                    contact_row1, contact_row2, contact_row3
                ],
                style={
                    'height':'300px',
                    'width':'100%',
                    'background-color':'seashell',
                }
            ),
            page_bottom()
        ]
        )
    
    return layout