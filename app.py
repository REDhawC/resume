import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.ZEPHYR])
server = app.server
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"])
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/kag")
                    ])
            ])
        ],
        fluid=True,
    ),
    color='whitesmoke',
    style = {'height': 75,'font-weight': 'bold', 'fontSize': 28, 'textAlign': 'center'}

)

app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == '__main__':
	app.run_server()