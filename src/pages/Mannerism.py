import dash
import dash_bootstrap_components as dbc
from .get_items import items
dash.register_page(__name__, path='/Mannerism', name='Mannerism')
def layout():
	carousel = dbc.Carousel(
		items=items('Mannerism'),
		className='carousel-fade',style={'width': '50%', 'height': '50%', 'padding-top': '70px', 'margin-left': 'auto', 'margin-right': 'auto'}
	)
	return carousel
