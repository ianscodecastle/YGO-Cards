import requests
import pandas as pd
import json
import re

# Connect to API and get json response
url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
cards = requests.get(url=url)
cards_json = cards.json()['data']

# Make dataframe from json response
cards_df = pd.DataFrame(cards_json)
# Column of card names
cards_names = cards_df['name']

# Explode nested card prices column into its own dataframe
cards_prices = pd.json_normalize(cards_df['card_prices'].explode())
# Add names column to new prices dataframe, then reorder to put names first
cards_prices = cards_prices.join(cards_names)
price_cols = ['name','cardmarket_price', 'tcgplayer_price', 'ebay_price', 'amazon_price', 'coolstuffinc_price']
cards_prices = cards_prices[price_cols]

# Make basic info df w/ image url
cards_images = pd.json_normalize(cards_df['card_images'].explode())
main_image = cards_images['image_url']
info_cols = ['name', 'level', 'attribute', 'type', 'race', 'archetype', 'atk', 'def', 'desc', 'image_url']
cards_info = cards_df.join(main_image)
cards_info = cards_info[info_cols]

def price_search():
    my_card = input()
    result = cards_prices.loc[cards_prices['name'].str.contains(my_card, case=False)]

    if result.empty:
        print(f'"{my_card}" was not found.')
    else:
        print(result)

def card_search():
    my_card = input()
    result = cards_info.loc[cards_info['name'].str.contains(my_card, case=False)]

    if result.empty:
        print(f'"{my_card}" was not found.')
    else:
        print(result)