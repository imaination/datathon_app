import dash_bootstrap_components as dbc
import dash
from dash import html, dcc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                #dbc.DropdownMenuItem("movement1", href="/movement1"),
		dbc.DropdownMenuItem("Academism", href="/Academism"),
		dbc.DropdownMenuItem("Art Nouveau", href="/Art Nouveau"),
		dbc.DropdownMenuItem("Baroque", href="/Baroque"),
		dbc.DropdownMenuItem("Expressionism", href="/Expressionism"),
		dbc.DropdownMenuItem("Hudson River School", href="/Hudson River School"),
		dbc.DropdownMenuItem("Impressionism", href="/Impressionism"),
                dbc.DropdownMenuItem("Mannerism", href="/Mannerism"),
                dbc.DropdownMenuItem("Neoclassicism", href="/Neoclassicism"),
                dbc.DropdownMenuItem("Orientalism", href="/Orientalism"),
                dbc.DropdownMenuItem("Post-Impressionism", href="/Post-Impressionism"),
                dbc.DropdownMenuItem("Pre-Raphaelite Brotherhood", href="/Pre-Raphaelite Brotherhood"),
		dbc.DropdownMenuItem("Realism", href="/Realism"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="DigitalAIArtGallery",
    #color="primary",
    color="#ff964f",
    dark=True,
    fixed="top",
)

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CYBORG])
server = app.server
app.layout = dbc.Container([
	dbc.Row([
		dbc.Col([
			html.H1('Welcome to the AI Generated Digital Art Gallery!', style={'textAlign': 'center', 'padding-top':'70px'}),
        		html.Div(children='''
                		AI Artworks inspired by Famous Artists and Movements.
        		''', style={'textAlign': 'center'}),
			]),

	]),
	html.Hr(),
	navbar,
	dash.page_container,
])


if __name__ == '__main__':
	app.run_server(debug=True, use_reloader=True) # Turn off reloader if inside Jupyter


