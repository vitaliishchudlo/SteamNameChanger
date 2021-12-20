import json
import os

PATH_TO_WEBDRIVER = os.getcwd().replace('\\\\', '\\') + '\\chromedriver.exe'


def get_data(USER_LOGIN=None, USER_PASSWORD=None):
    try:
        with open('config.json', 'r') as file:
            output = file.read()
            object_json = json.loads(output)

        if USER_LOGIN:
            return object_json['userdata']['username']

        elif not USER_PASSWORD:
            return object_json['userdata']['password']
    except Exception as err:
        pass


def get_user_login():
    try:
        with open('config.json', 'r') as file:
            output = file.read()
            object_json = json.loads(output)
        return object_json['userdata']['username']
    except Exception as err:
        print('Cant get user login')


def get_user_password():
    try:
        with open('config.json', 'r') as file:
            output = file.read()
            object_json = json.loads(output)
        return object_json['userdata']['password']
    except Exception as err:
        print('Cant get user password')


STEAM_AUTHORIZATION_PAGE = 'https://store.steampowered.com/login/'

MENU_CHOICE_1 = 'Starting program...'
MENU_CHOICE_2 = 'Changing Steam account'
MENU_CHOICE_3 = 'Changing nicknames set'
MENU_CHOICE_4 = 'Reset config.json file'
MENU_CHOICE_5 = 'Exiting program'
MENU_CHOICE_6 = 'Error....EXIT PROGRAM'
