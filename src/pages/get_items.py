import pandas as pd
import os


def items(start, end):
    PATH = os.path.dirname(os.getcwd())
    DATA_PATH = os.path.join(PATH, 'src/assets')
    gifs = 'gifs.csv'
    print(os.path.join(DATA_PATH, gifs))
    df = pd.read_csv(os.path.join(DATA_PATH, gifs))
    
    df = df.iloc[start:end]
    items = []
    for idx, rows in df.iterrows():
        movement_dict = {
            "key": str(idx),
            "src": rows['url'],
            "header": rows['header'],
            "caption": rows['caption'],
        }

        items.append(movement_dict)
    return items

