from dash import register_page
from dash_bootstrap_templates import load_figure_template
from components.containers import get_project_page_layout
import json
####################################################################################
with open("config/pages_config.json", "r") as f:
    pages_config = json.load(f)
### Register Page Name for Multi-Page Layout ###
register_page(__name__, path='/optionsport')


load_figure_template('FLATLY')

# Get page layout
layout = get_project_page_layout('optionsport', pages_config)