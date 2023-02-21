import dash
import dash_bootstrap_components as dbc
from .get_items import items
dash.register_page(__name__, path='/Mannerism', name='Mannerism')
def layout():
	carousel = dbc.Carousel(
		items=items(1,5),
		className='carousel-fade',style={'width': '80%', 'height': '70%', 'padding-top': '70px', 'margin-left': 'auto', 'margin-right': 'auto'}
	)
	return carousel
