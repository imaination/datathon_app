import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', name="Home")

def generate_card(movement, caption, image_link, link):
        card = dbc.Card(
        [
                dbc.CardImg(src=image_link, top=True),
                dbc.CardBody(
                        [
                                html.H4(movement, className="card-title"),
                                html.P(
                                        caption,
                                        className="card-text",
                                ),
                                dbc.Button(movement, external_link=False, href=link,  color="primary"),
                        ]
                ),
        ],
        style={"width": "18rem", "height": "50%"},
        )
        return card

cards = dbc.Row(
        [
                dbc.Col(generate_card("Symbolism", "A late 19th-century art movement of French and Belgiam origin in poetry and other arts seeking to represent absolute truths symbolically through language and metaphorical images.", "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Pierre+Auguste+Renoir/Le+Pont+Neuf+Paris.jpg", link='/movement1'), width="auto"),
                dbc.Col(generate_card("Intimism", "An artistic movement in the late 19th-century and early 20th-century that involved the depiction of banal yet personal domestic scenes, particularly those within domestic interiors.", "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Vincent+Van+Gogh/Peach+Trees+in+Blossom.jpg", link="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/#"), width="auto"),
	 ]
)


layout = html.Div([
	cards,
])
