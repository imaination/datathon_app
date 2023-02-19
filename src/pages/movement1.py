import dash
import dash_bootstrap_components as dbc

dash.register_page(__name__, name="movement1")


def layout():
	carousel = dbc.Carousel(
		items=[
			{"key": "1", "src": "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Vincent+Van+Gogh/Wheatfield+with+Crows.jpg", "header": "HEADER HERE", "caption": "caption here, maybe generate images to text",},
			{"key": "2", "src": "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Vincent+Van+Gogh/Cypress+against+a+Starry+Sky.jpg", "header": "HEADER HERE", "caption": "caption here, maybe generate images to text",},
			{"key": "3", "src": "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Vincent+Van+Gogh/A+Marsh.jpg", "header": "HEADER HERE", "caption": "caption here, maybe generate images to text",},
		],
		className="carousel-fade",
		style={"width": "80%", "height": "70%", "padding-top": "70px", "margin-left": "auto", "margin-right": "auto"}
	)
	return carousel
