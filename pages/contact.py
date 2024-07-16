from dash import register_page
from dash_bootstrap_templates import load_figure_template
import json

#my imports
from components.containers import get_contact_layout


####################################################################################

# Load Config File
with open("config/other_pages_config.json", "r") as f:
    other_config = json.load(f)

### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/contact')

# Set Template
load_figure_template('FLATLY')

### Begin Page Layout ###
layout = get_contact_layout(other_config)

####################################################################################

