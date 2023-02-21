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
                                dbc.Button(movement, external_link=False, href=link, color="warning"),
                        ]
                ),
        ],
        style={"width": "18rem", "height": "35rem", "overflow": "scroll"},
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
        cards.append(dbc.Col(generate_card(movement, description, img, link='/{}'.format(movement)), style={"width":"auto"} ))

    return cards

# Access csv with famous movements
PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PATH, "src/assets/unique_movements.csv")
movements_df = pd.read_csv(DATA_PATH)

cards_gen = dbc.Row(
	generate_card_list(movements_df),
)

layout = html.Div([
	cards_gen,
])
