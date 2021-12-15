import json
import os

PATH_TO_WEBDRIVER = os.getcwd().replace('\\\\', '\\') + '\\chromedriver.exe'


def get_data(USER_LOGIN=None, USER_PASSWORD=None):
    with open('config.json', 'r') as file:
        output = file.read()
        object_json = json.loads(output)

    if USER_LOGIN:
        return object_json['userdata']['username']

    elif USER_PASSWORD:
        return object_json['userdata']['password']


USER_LOGIN = get_data(USER_LOGIN=True)
USER_PASSWORD = get_data(USER_PASSWORD=True)

STEAM_AUTHORIZATION_PAGE = 'https://store.steampowered.com/login/'
