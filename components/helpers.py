import dash_bootstrap_components as dbc
from dash import html, get_asset_url
import json

# Load Needed Data
with open("config/portfolio_page_config.json", "r") as f:
    portfolio_page_config = json.load(f)

# Primary Functions #
def read_text(file_path):
    """
    Read text data from data directory
    """
    with open(file_path, 'r') as file:
        return file.read()

def Navbar():
    """
    Generate Main Webpage Navbar

    Returns
    -------
    dash.html object
        Object representing
    """
    layout = html.Div(
        [
        dbc.NavbarSimple(
            children=[
                get_navbar_item("HOME","/"),
                get_navbar_item("PORTFOLIO","/portfolio"),
                get_navbar_item("ABOUT","/about")
            ],
            brand="DYLAN JORLING, CFA",
            color="#004640",
            brand_style={
                    'color': 'white',
                    'font-size': '45px',
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    'font-weight': 'bold',
                    'letter-spacing': '-2px',
                    'padding':'0px'
            },
            style={
                'border-top':'3px solid #ae5000',
                'padding':'0px',
                'margin':'0px'
                },

        ),
        dbc.Row(
            [
            dbc.Col(
                html.H2(
                    '',
                    style={
                        'color': 'linen',
                        'font-size':'12px'
                    }
                ),
                style={
                    'background-color':'#004640',
                    'border-bottom': '3px solid #ae5000',
                    'textAlign':'center',
                    'width':'33%'
                }
            ),
            dbc.Col(
                html.H2(
                    'QUANTITATIVE FINANCE | DEEP LEARNING | DATA SCIENCE',
                    style={
                        'color': 'linen',
                        'font-size':'12px'
                    }
                ),
                style={
                    'background-color':'#004640',
                    'border-bottom': '3px solid #ae5000',
                    'textAlign':'center',
                    'width':'34%'
                }
            ),
            dbc.Col(
                children=[
                    html.A(
                        "RESUMÉ",
                        href="/assets/resume.pdf",
                        style={
                            'color': 'linen',
                            'font-size':'15px',
                            'padding':'0px 20px 0px 10px'
                        }
                    ),
                    html.A(
                        "CONTACT",
                        href="/contact",
                        style={
                            'color': 'linen',
                            'font-size':'15px',
                            'padding':'0px 0px 0px 10px'
                        }
                    ),
                ],
                style={
                    'background-color':'#004640',
                    'border-bottom': '3px solid #ae5000',
                    'font-color': 'linen',
                    'textAlign':'center',
                    'padding':'0px 0px 0px 0px',
                    'width':'33%'
                }
                
            ),
        ],
        style={
            'textAlign':'center'
        }),])

    return layout

def proj_image(src, height='75%', width='75%'):
    """
    Format project image and return

    Parameters
    ----------
    src : str
        Path to the image
    height : str
        Percentage height to use
    width : str
        Percentage width to use
    
    Returns
    -------
    dash container
        Returns dash container with image in proper format
    """
    image_container = html.Div(
        children=[
            html.Img(
                src=r'assets/{}'.format(src),
                style={
                    'padding':'3px',
                    'height':height,
                    'width':width,
                    'border':'2px solid burlywood',
                    'margin':'0px 0px 5px 0px'
                    }),])
    return image_container

def proj_buttons(href1, href2, href3=None, button3='Dashboard'):
    """
    Create buttons for project page.

    Arguments
    ---------
    href1 : str
        first button link
    href2: str
        second button link
    href3 : str; optional
        third button link. Default to None
    button3 : str; optional
        third button name. Default to 'Dashboard'

    Returns
    -------
    html.Div
        html.Div object containing proper button objects
    """
    # Create first two buttons
    buttons = [
        button_with_link("Overview", href1),
        button_with_link("Code", href2),
    ]

    # Add third button if passed
    if href3:
        buttons.append(button_with_link(button3, href3))
    
    # Create button container and return it
    button_container = html.Div(
        children=buttons,
        style={
            'padding':'0px 0px 10px 0px',
            'textAlign':'center'
        }
    )
    return button_container

# Helper Functions
def button_with_link(text, href, padding='0px 15px 0px 0px', new_tab=False):
    """
    Create dash.html object representing a button with a link behind it

    Parameters
    ----------
    text : str
        Text to be on button
    href : str
        Text representing the button link
    padding : str; optional
        represents the padding of the button
    new_tab: bool; optional
        if True, the link will open in a new tab. Default False

    Returns
    -------
    dash.html object
        Returns dash.html object representing the button with a link
    """
    # Check tab configuration
    if new_tab == True:
        target = '_blank'
    else:
        target = None

    button_with_link = html.A(
        button(text),
            href=href,
            target=target,
            style={
                'padding':padding,
                'textAlign':'center'
            }
        )
    return button_with_link

def get_buttons(arg_list):
    """
    Given a set of arguments, return proper button configuration

    This function faciliates arguments from the project page configuration to get correct buttons.

    Parameters
    ----------
    arg_list : list of str
        List of string arguments for defining buttons on the project layout

    Returns
    -------
    dash.html object

    """
    if len(arg_list) == 2:
        return proj_buttons(arg_list[0], arg_list[1])
    elif len(arg_list) == 3:
        return proj_buttons(arg_list[0], arg_list[1], arg_list[2])
    elif len(arg_list) == 4:
        return proj_buttons(arg_list[0], arg_list[1], arg_list[2], button3=arg_list[3])
    else:
        raise ValueError("Invalid number of button arguments passed!")

def button(text):
    """
    Format button for Project Page

    Parameters
    ----------
    text : str
        Text to be on button
    
    Returns
    -------
    dash.html object
        Returns dash.html object representing the button
    """
    button = html.Button(
        text,
        style={
                'color':'white',
                'font-size':'20px',
                'background-color':'#666600',
            },
    )
    return button

def get_navbar_item(text, href):
    """
    Returns NavBar Item for main NavBar
    """
    navbar_item = dbc.NavItem(
        dbc.NavLink(
            text,
            href=href,
            style={
                'color':'white',
                'font-size': '22px',
                'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                'font-weight':'bold'
            }
            )
            )
    return navbar_item

def get_bottom_nav_item(text, href, im_path):
    """
    Creates items for bottom navigation bar

    Parameters
    ----------
    text : str
        name of button
    href : str
        button link path
    im_path : str
        path to image that button will display
    """
    bottom_nav_item = html.A(
        href=href,
        children=[
            html.Img(
                src=get_asset_url(im_path),
                alt=text,
                style={
                    'color': 'white',
                    'margin':'5px 5px 3px 0px',
                    'height':'50px'
                })])

    return bottom_nav_item

def dashboard_navbar(name, col1, col2, col3):
    navbar = html.Div(
                [
                dbc.Row(
                    dbc.Col(
                        children=[
                            
                            html.A(
                                "Documentation",
                                href="/{}/dashboard/documentation".format(name),
                                style={
                                    'padding':'0px 5px 0px 0px',
                                    'color':col2
                                }
                            ),

                            html.A(
                                "Overview",
                                href="/{}".format(name),
                                style={
                                    'padding':'0px 5px 0px 5px',
                                    'color':col2
                                }
                            ),

                            html.A(
                                "Portfolio",
                                href="/portfolio",
                                style={
                                    'padding':'0px 30px 0px 5px',
                                    'color':col2
                                }
                            ),
                        ],
                        style={
                            'background-color':col1,
                            'border-bottom': '3px solid {}'.format(col3),
                            'font-color': col2,
                            'font-size':'18px',
                            'textAlign':'right',
                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                            'font-weight':'bold',
                            'width':'110%'
                            
                        }
                    ),
                )
                ]
            )

    return navbar

def dashboard_navbar2(name, col1, col2, col3):
    navbar = html.Div(
                [
                dbc.Row(
                    dbc.Col(
                        children=[
                            
                            html.A(
                                "Dashboard",
                                href="/{}/dashboard".format(name),
                                style={
                                    'padding':'0px 5px 0px 0px',
                                    'color':col2
                                }
                            ),

                            html.A(
                                "Overview",
                                href="/{}".format(name),
                                style={
                                    'padding':'0px 5px 0px 5px',
                                    'color':col2
                                }
                            ),

                            html.A(
                                "Portfolio",
                                href="/portfolio",
                                style={
                                    'padding':'0px 30px 0px 5px',
                                    'color':col2
                                }
                            ),
                        ],
                        style={
                            'background-color':col1,
                            'border-bottom': '3px solid {}'.format(col3),
                            'font-color': col2,
                            'font-size':'18px',
                            'textAlign':'right',
                            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                            'font-weight':'bold',
                            'width':'110%'
                            
                        }
                    ),
                )
                ]
            )

    return navbar
################################# Helper Functions for Individual Project Pages ######################################
def get_project_title_container(title):
    """
    Get row formatted for individual project page

    Parameters
    ----------
    title : str
        The full, formatted name of the project

    Returns
    -------
    dbc object
        returns dbc object representing project title container
    """
    title_row = dbc.Row([
        dbc.Col(
            html.H2(
                title,
                style={
                    'font-size':'30px',
                    'color':'#ae5000',
                    'font-weight':'bold'
                }
                ),
                style={
                    'margin':'30px 30px 0px 30px',
                    }),])
    return title_row

def get_proj_pages_buttons(button_list):
    """
    Create buttons for individual project pages.

    Parameters
    ---------
    button_list : list of dict
        list of dict, each containing a button name as key and button link as value

    Returns
    -------
    html.Div
        html.Div object containing proper button objects
    """
    # Get button objects
    if len(button_list) == 1:
        paddings=['0px 15px 0px 30px']
    elif len(button_list) == 2:
        paddings = ['0px 15px 0px 30px', '0px 0px 0px 15px']
    else:
        paddings = ['0px 15px 0px 30px', '0px 15px 0px 15px', '0px 0px 0px 15px']
    buttons = [button_with_link(list(d.keys())[0], list(d.values())[0], paddings[i]) for i, d in enumerate(button_list)]

    # Format buttons in a container
    button_container = html.Div(
        children=buttons,
         style={
             'padding':'15px 0px 15px 0px',
             'textAlign':'left'
             })

    return button_container

def get_all_project_content_section_containers(content_section_list, project):
    """
    Get all section containers

    Parameters
    ----------
    content_section_list : list of dict
        Section configuration list
    project : str
        String representing project name in config file

    """
    # Iterate over content section list and return list of section containers
    all_content_container = []
    for content_section_dict in content_section_list:
        h, c = get_project_content_section_container(content_section_dict, project)
        all_content_container.append(h)
        all_content_container.append(c)
    return all_content_container

def get_project_content_section_container(content_section_dict, project):
    """
    Get container for a full section within a project
    """
    # Load header and content list
    header, content_list = content_section_dict.popitem()

    # Get section name
    section = header.lower().replace(" ","_")

    # Create empty list for storing container
    section_containers = []

    # Iterate through content list and append containers
    for item in content_list:
        if isinstance(item, str):
            # Only paragraph items are strings, so get paragraph container
            filepath = f"data/{project}/content/{section}_{item}.txt"
            section_containers.append(get_paragraph_container(filepath))
        elif isinstance(item, dict):
            if isinstance(list(item.values())[0], dict):
                # If there is an inner dict, we know this is a dual image container
                section_containers.append(get_dual_image_container(item, project, section))
            else:
                # Otherwise, this is a single image container
                section_containers.append(get_image_container(item, project, section))
        elif isinstance(item, list):
            # Only bulleted list content are lists in config
            section_containers.append(get_list_item_container(item))
    # Create section container and append header container
    header_container = get_project_content_section_header_container(header)

    # Wrap section containers in a row container
    content_container = dbc.Row([
        dbc.Col(
            section_containers,
            style={
                    'margin':'0px 30px 15px 30px',
                    'background-color':'#faf0e6'
                    }
                )],

    )

    return header_container, content_container

def get_project_content_section_header_container(section_title):
    """
    Get section header container for project pages

    Parameters
    ----------
    section_title : str
        Section header text

    Returns
    -------
    dbc.Row object
        dbc object representing header container
    """
    header_container = dbc.Row([
        dbc.Col(
            html.H2(
                section_title,
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
        
    ])

    return header_container

def get_image_container(im_dict, project, section):
    """
    Given an im_dict from the config file, return an image container

    Parameters
    ----------
    im_dict : dict
        dictionary with src as key and either height or width % as value
    project: str
        String representing project name in config file
    section : str
        Name of section image will be located in
    

    Returns
    -------
    dash.html.Img object
        returns dash object representing image container
    """
    # Extract src and value
    src, val = im_dict.popitem()
    style={
            'border':'#ae5000 solid 2px',
            'margin':'15px',
        }
    if isinstance(val, int):
        style['height'] = f"{str(val)}px"
    else:
        style['width'] = val
    
    # Create image container
    image_container = html.Div([
        html.Img(
            src=f"assets/{project}_{section}_{src}.png",
            style=style
            ),
    ],
    style={'textAlign':'center'},
    )

    return image_container

def get_dual_image_container(ims_dict, project, section):
    """
    Given an ims_dict from the config file, return a dual image container

    Parameters
    ----------
    im_dict : dict
        dictionary with src as key and either height or width % as value
    project: str
        String representing project name in config file
    section : str
        Name of section image will be located in

    Returns
    -------
    dash.html.Div object
        returns dash object representing image container for two images
    """
    # Get src root
    _, ims = ims_dict.popitem()
    srcs = list(ims.keys())

    # Set Style
    style = {
        'font-size':'22px',
        'border':'#ae5000 solid 2px',
        'margin':'15px',
        'display':'inline-block',
        'width':'38%'
    }

    # Format Container
    dual_image_container = html.Div([
        html.Img(
            src=f"assets/{project}_{section}_{srcs[0]}.png",
            style=style
        ),
        html.Img(
            src=f"assets/{project}_{section}_{srcs[1]}.png",
            style=style
        )
        ],
        style={
            'textAlign':'center'
        }
    )
    return dual_image_container

def get_paragraph_container(file_path):
    """
    Given a file path containing paragraph text, return a container for this paragraph

    Parameters
    ----------
    file_path : str
        file path where text is located

    Returns
    -------
    dash.html.P object
        dash object representing paragraph container
    """
    # Set style at top for easy configuring
    style = {
        'font-size':'16px',
        'color':'#666600',
        'textAlign':'left'
    }

    # Load text
    text = read_text(file_path)

    # Create container and return
    paragraph_container = html.P(
        text,
        style=style
    )
    return paragraph_container

def get_list_item_container(list_items):
    """
    Given a list of items, return a formatted bulleted list

    Parameters
    ----------
    list_items: list of str
        Bullet points to format
    """
    # Get style for each list item:
    style = {
        'font-size':'16px',
        'color':'#666600',
        'textAlign':'left'
    }

    # Create the unordered list (ul) with list items (li)
    bullet_list = html.Ul(
        [html.Li(item, style=style) for item in list_items],
        style={
            'list-style-position':'outside',
            'list-style-type':'square',
        }
        )
    return bullet_list

def get_all_project_skills_container(skills_list, project):
    """
    Create Skills Container for individual project pages

    Parameters
    ----------
    skills_list : list of dict
        list of dict, each containing a skill name as key and description as a value
    project: str
        String representing project name in config file
    """
    # Iterate through skills list to get all skill list items
    skill_items = []
    for skill in skills_list:
        skill_title, skill_description = get_skill_item_from_dict(skill, project)
        skill_items.append(get_skill_item_container(skill_title, skill_description))

    skills_container = dbc.Row(
        [
            dbc.Col([
                html.H2(
                    "Skill Highlights",
                    style={
                        'font-size':'22px',
                        'color':'#666600'
                    }
                ),
                html.Ul(
                    skill_items,
                    style={
                        'list-style-position':'outside',
                        'list-style-type':'square',
                    }
                    ),
                    ],
                    style={
                            'margin':'0px 30px 0px 30px',
                            'background-color':'#faf0e6',
                            'list-style-type':'square',
                        }
                ),
                ],
            )
    return skills_container

def get_skill_item_from_dict(skill_item_dict, project):
    """
    Given a skill item dict return the proper skill title and description

    Parameters
    ----------
    skill_item_dict : dict
        Dict with a skill title as a key and skill description as a value
    project: str
        String representing project name in config file

    Returns
    -------
    tuple
        Returns tuple of (skill_title, skill_description)
    """
    k, v = skill_item_dict.popitem()
    if k == 'lib':
        skill_description = v
        return "Libraries/Modules", skill_description
    else: 
        skill_title = v
        skill_description = read_text(f"data/{project}/skills/{k}.txt")
        return skill_title, skill_description

def get_skill_item_container(skill_title, skill_description):
    """
    Create container object for single skill item

    Parameters
    ----------
    skill_title : str
        Title of Skill
    skill_description : str
        Description of skill

    Returns
    -------
    dash.html.Li object
        Returns dash container representing list item for the skill/description
    """
    skill_item_container = html.Li(
        html.Div([
            html.Span(
                skill_title + ": ",
                style={
                    'color':'#004640',
                    'font-weight':'bold'
                },
                ),
                skill_description,
                ],
                style={
                    'color':'#ae5000',
                    'font-size':'16px',
                    'textAlign':'left',
                    'padding':'5px',
                    
                }
            ),
        )
    return skill_item_container

def get_page_bottom_container():
    """
    Get bottom page row container

    Returns
    -------
    """
    bottom_row_container = dbc.Row(
        style={
                'background-color':'seashell',
                'height':'300px',   
                'width':'110%'
            }
        )
    return bottom_row_container

################################# Helper Functions for Other Pages ######################################
def get_about_left_container(about_section_content_dict):
    """
    Get left side container for the About Page
    """
    about_left_container = dbc.Col(
            dbc.Stack(
                [
                    html.Div(
                        children=[
                            get_about_image_container(),
                            *get_about_areas_of_interest_container(about_section_content_dict[0]),
                            *get_about_areas_of_interest_container(about_section_content_dict[1])
                        ]
                    )
                ]
            ),
            style={
                'background-color':'#faf0e6',
                'margin':'0px 45px 15px 15px',
                'width':'80%',
                'textAlign':'center'
            }

        )

    return about_left_container

def get_about_right_container(bio_dict):
    """
    Get right side container for About Page
    """
    # Pop header and content bullet list
    header, content = bio_dict.popitem()

    # Add Bio Header
    children = [get_about_section_header_container(header)]

    # Define Bio content style
    style={
        'color':'#ae5000',
        'font-size':'17px',
        'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
        'textAlign':'left',
        'padding':'0px'
    }

    # Add Bio Content
    for content in content:
        file_path = f"data/about/content/bio_{content}.txt"
        children.append(html.P(read_text(file_path), style=style))

    about_right_container = dbc.Col(
        dbc.Stack(
            children
        ),
        style={
            'background-color':'#faf0e6',
            'margin':'0px 45px 15px 15px',
            'width':'80%',
            'textAlign':'center'
        }
    )
    return about_right_container

def get_about_image_container():
    image_container = html.Img(
        src='assets/about.png',
            style={
                'padding':'3px',
                'height':'75%',
                'width':'75%',
                'border':'2px solid burlywood',
                'margin':'15px 0px 15px 0px'
            }
        )
    
    return image_container

def get_about_areas_of_interest_container(aoi_dict):
    """
    Return the Areas of Professional & Academic Interest Container
    """
    # Pop header and content bullet list
    header, content = aoi_dict.popitem()
    aoi_containers = [get_about_section_header_container(header)]
    content_bullets = [html.Li(x) for x in content]
    content_container = html.H4(
        content_bullets,
        style={
            'color':'#ae5000',
            'font-size':'20px',
            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
            'textAlign':'left',
            'padding':'0px',
            'list-style-type':'square'
        }
    )
    # Append content to area of interest container list
    aoi_containers.append(content_container)
    return aoi_containers

def get_about_personal_container(personal_dict):
    """
    Return the Personal content container
    """
    header, _ = personal_dict.popitem()
    personal_containers = [get_about_section_header_container(header)]

    # Load text
    file_path = "data/about/content/aoi_p1.txt"
    text = read_text(file_path)

    style={
        'color':'#ae5000',
        'font-size':'18px',
        'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
        'textAlign':'left',
        'padding':'0px'
    }

    paragraph_container = html.P(
        text,
        style=style
    )
    # Append content to personal container list
    personal_containers.append(paragraph_container)

    return personal_containers 

def get_about_section_header_container(header):
    header_container = html.H4(
        header,
        style={
            'font-size':'24px',
            'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
            'font-weight':'bold',
            'textAlign':'left',
            'color':'#666600',
            'padding':'15px 0px 0px 0px'
        }
    )

    return header_container

def get_about_header():
    """
    Return header for the about page
    """
    about_header = dbc.Row(
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
    )

    return about_header

def get_about_button_container(button_list):
    """
    Get button container for the about page
    """
    button_container =  html.Div(
        children=[
            get_proj_pages_buttons(button_list)
        ],
        style={
            'textAlign':'center',
            'padding':'0px 0px 300px 0px',
        }
    )
    return button_container

def get_contact_top_containers(other_config):
    """
    Get contact top container
    """
    # Get top row of container
    contact_top_container = dbc.Row([
        dbc.Col(
            html.H2(
                '',
                style={

                }
            ),
            style={

                'textAlign':'center'
            }
        ),
        ],
        style={
            'height':'0px',
            'width':'100%'
            }
    )

    # Return next row of container
    contact_next_container = dbc.Row(
        style={
            'background-image':f'url("assets/{other_config["contact"]["image"]}")',
            'bacgkround-repeat':'no-repeat',
            'background-size': 'cover',
            'background-position': 'left bottom',
            'max-width':'120%',
            'max-height':'110%',
            'height':'450px',
            'border-bottom': '3px solid #ae5000',
            }
            )

    return contact_top_container, contact_next_container

def get_contact_bottom_container(other_config):
    """
    Get bottom row of Contact page container
    """
    contact_bottom_container = dbc.Row([
        dbc.Col([
            html.H2(
                [
                html.U("Contact"),
                ],
                style={
                    'color': '#666600',
                    'font-size':'35px',
                    'padding':'10px 0px 0px 60px',
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    'font-weight':'bold'
                    
                }
            ),
            html.H2(
                [
                f"Email: {other_config['contact']['email']}",
                ],
                style={
                    'color':'#666600',
                    'font-size':'25px',
                    'padding':'0px 0px 5px 60px',
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    'font-weight':'bold'
                    }
                )
            ],
            style={
                'textAlign':'left'
            }
        ),
        ],
        style={
            'height':'300px',
            'width':'100%',
            'background-color':'seashell',
        }
    )

    return contact_bottom_container

def get_home_top_container(other_config):
    """
    Get top container for home page
    """
    home_top_container = [dbc.Row([
        dbc.Col(
            html.H2(
                '',
                style={

                }
            ),
            style={

                'textAlign':'center'
            }
        ),
        ],
        style={
            'height':'0px',
            'width':'100%'
            }
    ),
    dbc.Row([
        dbc.Col(
            html.H2([
                'Transforming',
                html.Br(),
                'Data',
                html.Br(),
                'Into',
                html.Br(),
                'Knowledge.'
                ],
                style={
                    'color': 'white',
                    'padding':'90px 0px 0px 250px',
                    'font-size':'45px',
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    'font-weight':'bold'
                }
            ),
            style={
                'textAlign':'left'
            }
        ),
        ],
        style={
            'background-image':f'url("assets/{other_config["home"]["image"]}")',
            'bacgkround-repeat':'no-repeat',
            'background-size': 'cover',
            'background-position': 'left bottom',
            'max-width':'120%',
            'max-height':'110%',
            'height':'450px',
            'border-bottom': '3px solid #ae5000'
            }
    )]
    return home_top_container

def get_home_bottom_container():
    """
    Get bottom container for home page
    """
    home_bottom_container = [dbc.Row([
        dbc.Col([
            html.H2(
                "WELCOME.",
                style={
                    'color': '#ae5000',
                    'font-size':'50px',
                    'padding':'30px 0px 5px 60px',
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    'font-weight':'bold'
                    
                }
            ),
            html.H2(
                "Click \"Portfolio\" to view my Projects and Dashboards.",
                style={
                    'color': '#666600',
                    'font-size':'30px',
                    'padding':'5px 0px 200px 60px',
                    'font-family': 'Montserrat, Helvetica, Arial, sans-serif',
                    }
                )
            ],
            style={
                'textAlign':'left'
            }
        ),
        ],
        style={
            'height':'300px',
            'width':'100%',
            'background-color':'seashell',
        }
    ),
    dbc.Row(
        style={
            'padding':'0px 0px 200px 0px'
            }
    )]
    return home_bottom_container
# Remove later
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

def page_bottom(col1='#666600', col2='#ae5000', col3='white'):
    bottom = dbc.Stack(
                [
                dbc.Col(
                    children=[
                        html.A(
                            href="https://www.linkedin.com/in/dylan-jorling-cfa-75729045/",
                            children=[
                                html.Img(
                                    src=get_asset_url('li.png'),
                                    alt="Link to my LinkedIn",
                                    style={
                                        'color': 'white',
                                        'margin':'5px 5px 3px 0px',
                                        'height':'50px'
                                    }
                                )
                            ]
                        ),
                        html.A(
                            href="https://github.com/dkjorling",
                            children=[
                                html.Img(
                                    src=get_asset_url('gh.png'),
                                    alt="Link to my GitHub",
                                    style={
                                        'color': 'white',
                                        'padding':'5px 0px 3px 5px',
                                        'height':'50px'
                                    }
                                ),
                            ]
                        )
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



def project_section_layout(section_title, text_path):
    project_section = 0

