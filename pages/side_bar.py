import dash
from dash import html
import dash_bootstrap_components as dbc
SIDEBAR_STYLE = {
    "backgroundColor": "whitesmoke",
    "width": "10rem",
}

def sidebar():
    nav_links = []
    for page in dash.page_registry.values():
        if page["path"].startswith("/kag"):
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
        elif page["path"]=="/projects":
            nav_links.append(
                dbc.NavLink(
                    [
                        html.Div("Financial Dashboard web app", className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
            )
    return dbc.Nav(children=nav_links,
                   vertical=True,
                   pills=True,
                   className="page-link",
                   style=SIDEBAR_STYLE)