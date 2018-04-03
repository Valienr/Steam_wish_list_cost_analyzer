import re
from bs4 import BeautifulSoup
import json
import requests
from datetime import date


def get_wishlist(steam_id):
    """ получаем список игр из вишлиста вводая публичный стим id """
    url = "http://steamcommunity.com/profiles/{}/wishlist".format(steam_id)
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    print(soup.title.string)
    foo = soup.find(string=re.compile("var g_rgWishlistData = ")).split(';')[0][25:]
    l = eval(foo)
    temp = []
    for item in l:
        temp.append(item['appid'])
    return temp #[250620, 274940, 329430, 448510, 578080]


def get_game_id_time_price(game_list):
    data_for_graf = []
    now = date.today().strftime("%y.%m.%d")
    game_data = {}
    for g in game_list:
        req = requests.get('http://store.steampowered.com/app/{}/'.format(g), cookies=cookie).text
        soup = BeautifulSoup(req, 'html.parser')
        foo = soup.find(itemprop="price") #<meta content="509" itemprop="price"/>
        # print(foo)
        temp = str(foo).split('"') #['<meta content=', '509', ' itemprop=', 'price', '/>']
        # print(temp)
        if temp == ['None']:
            game_data["game id"] = g
            game_data["date"] = 'None'
            game_data["price"] = 'None'
            pass
        else:
            game_data["game id"] = g
            game_data["date"] = now
            game_data["price"] = temp[1]
        data_for_graf.append(game_data)
        # game_data = {}
    return data_for_graf


def get_cookies(item):
    """
     получаем куки
     сейчас не используется файл куки сохранён в корне
     """
    session = requests.session()
    p = session.post("http://store.steampowered.com/agecheck/app/{0}/".format(item))
    # print('headers', p.headers)
    print('cookies', requests.utils.dict_from_cookiejar(session.cookies))
    # print('html',  p.text)
    cook = requests.utils.dict_from_cookiejar(session.cookies)
    return cook


def store_data(value):
    """ сохраняем данные в json """
    file = 'game_data.json'
    with open(file, 'a') as f_obj:
        if len(value[0]) == 0:
            print("пусто")
            pass
        else:
            json.dump(value, f_obj)
            print('ok')


def load_gamedata():
    """ загружаем файл для анализа """
    filename = 'game_data.json'
    with open(filename) as f:
        plot_dicts = json.load(f)
        print(plot_dicts)


def load_cookie():
    filename = 'cookie.json'
    with open(filename, 'r') as f:
        cookie = json.load(f)
        return cookie


id = '76561198129539168'  # id пользователя

# http://steamcommunity.com/profiles/76561198175913657
# http://steamcommunity.com/profiles/76561198129539168



cookie = load_cookie()

print('-------games-------')
games = get_wishlist(id)  # получаю список игр
print(games)


print('------list_for_analiz--------')
# list_for_analiz = get_game_id_time_price(games)
list_for_analiz = get_game_id_time_price([250620, 274940, 329430, 448510, 578080])
print(list_for_analiz)





# store_data(list_for_analiz) # сохраняем данные