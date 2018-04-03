import datetime
import requests
from bs4 import BeautifulSoup
import json
import datetime
from matplotlib import pyplot as plt
from datetime import datetime
import pygal
from pandas.io.json import json_normalize

filename = 'game_data.json'
with open(filename) as f:
    plot_dicts = json.load(f)
    print(plot_dicts)


bar = []
games = [250620, 27440, 329430, 448510, 578080]
for game in games:
    foo, prices, dates = [], [], []
    for dict in plot_dicts:
        if dict.get('game id') == str(game):
            prices.append(int(dict.get('price')))
            dates.append(dict.get('date'))
    foo.append([str(game), prices, dates])
    # print(foo)
    bar.append(foo)
print(bar)
