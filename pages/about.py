from dash import register_page
from dash_bootstrap_templates import load_figure_template
import json
from components.containers import get_about_container_layout

####################################################################################

# Load Config File
with open("config/other_pages_config.json", "r") as f:
    other_config = json.load(f)

### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/about')

# Set Template
load_figure_template('FLATLY')

# Get page layout
layout = get_about_container_layout(other_config)

####################################################################################