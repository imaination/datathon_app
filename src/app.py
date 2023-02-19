import dash_bootstrap_components as dbc
import dash
from dash import html, dcc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("movement1", href="/movement1", external_link=True,),
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

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.layout = html.Div([
		dash.page_container,
		navbar,
])

#for page in dash.page_registry.values():
#	print('path: ' + page["path"])
#	print(dcc.Link(children=page['name'], href=page['path']))


if __name__ == '__main__':
	app.run_server(debug=True, use_reloader=False) # Turn off reloader if inside Jupyter


