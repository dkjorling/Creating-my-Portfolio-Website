import dash_bootstrap_components as dbc
from dash import Dash, html, page_container

# my imports

# colors i like: powder blue: #63acff turq: #35fed6
# colors cont: dark gray: #004640, grbr: #6666004
# browns: redbr: #ae5000, tan:#deb887,
# lights: linen: #faf0e6, darker
################################################################################################################################

app = Dash(__name__, use_pages=True, assets_folder='assets', external_stylesheets=[dbc.themes.FLATLY])

#application = app.server # added for amazon beanstalk

# Expose the Flask server instance used by Dash
server = app.server

app.layout = html.Div(
                children=[
                    page_container,
                ],
            )


if __name__ == '__main__':
    app.run_server(debug=False, port=8080)  # port added for amazon beanstalk
                       
