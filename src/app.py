import dash_bootstrap_components as dbc
import dash
from dash import html, dcc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="http://127.0.0.1:8050")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("movement1", href="http://127.0.0.1:8050/movement1"),
                dbc.DropdownMenuItem("movement2", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="DigitalAIArtGallery",
    color="primary",
    dark=True,
    fixed="top",
)

server = app.server
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div([
		dash.page_container,
		navbar,
		
])

if __name__ == '__main__':
	app.run_server(debug=True, use_reloader=False) # Turn off reloader if inside Jupyter


