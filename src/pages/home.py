import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import os

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
        style={"width": "18rem", "height": "100%"},
        )
        return card


# function to generate a list of cards
def generate_card_list(df):
    # Initiate empty list to store card information
    cards = []
    
    for row in range(len(df)):
        movement = df.movement[row]
        description = df.description[row]
        img = df.image_url[row]
        cards.append(dbc.Col(generate_card(movement, description, img, link='/{}'.format(movement)),width="auto"))

    return cards

# Access csv with famous movements
PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PATH, "src/assets/unique_movements.csv")
movements_df = pd.read_csv(DATA_PATH)

cards_gen = dbc.Row(
	generate_card_list(movements_df)
)

#cards = dbc.Row(
#        [
#                dbc.Col(generate_card("Symbolism", "A late 19th-century art movement of French and Belgiam origin in poetry and other arts seeking to represent absolute truths symbolically through language and metaphorical images.", "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Pierre+Auguste+Renoir/Le+Pont+Neuf+Paris.jpg", link='/movement1'), width="auto"),
#                dbc.Col(generate_card("Intimism", "An artistic movement in the late 19th-century and early 20th-century that involved the depiction of banal yet personal domestic scenes, particularly those within domestic interiors.", "https://kuleuven-datathon-2023.s3.eu-central-1.amazonaws.com/images/Vincent+Van+Gogh/Peach+Trees+in+Blossom.jpg", link="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/#"), width="auto"),
#	 ]
#)


layout = html.Div([
	#cards,
	cards_gen,
])
