import dash
import dash_bootstrap_components as dbc
from .get_items import items
dash.register_page(__name__, path='/Hudson%20River%20School', name='Hudson River School')
def layout():
	carousel = dbc.Carousel(
		items=items('Hudson River School'),
		className='carousel-fade',style={'width': '50%', 'height': '50%', 'padding-top': '70px', 'margin-left': 'auto', 'margin-right': 'auto'}
	)
	return carousel
