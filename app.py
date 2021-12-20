import os
import sys

from selenium import webdriver

import data
from api_steam import authorize_user
from data import MENU_CHOICE_1, MENU_CHOICE_2, MENU_CHOICE_3, MENU_CHOICE_4, MENU_CHOICE_5, MENU_CHOICE_6
from open_browser_pages import open_authorization_page
from scripts import create_chrome_webdriver, create_config_file, \
    hide_browser_window, check_user_data, check_status_authorized


def file_management():
    if not os.path.isfile('chromedriver.exe'):
        create_chrome_webdriver()

    if not os.path.isfile('config.json'):
        create_config_file()


def settings():
    try:
        file_management()
        # data.PATH_TO_WEBDRIVER - like: "D:\\Folder\\Projects\\Python\\SteamNameChanger"
        path_to_webdriver = data.PATH_TO_WEBDRIVER
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear some log in console
        if not hide_browser_window(options):
            os.remove('config.json')
            settings()
        global driver
        driver = webdriver.Chrome(executable_path=path_to_webdriver, options=options)
    except Exception as err:
        os.system('cls')
        print(f'\n\n {err}')


def steam_login():
    import ipdb; ipdb.set_trace() # BEFORE CHECK USER DATA
    if not check_user_data():
        import ipdb; ipdb.set_trace()  # BEFORE FILE MANAGEMENT
        file_management()
        import ipdb; ipdb.set_trace()  # BEFORE STEAM LOGIN
        steam_login()
    try:
        open_authorization_page(driver)
        if not authorize_user(driver):
            return False
        return True
    except Exception as err:
        print('Error when authorization in the SteamAccount', err)


def menu():

    os.system('cls')
    print('         STEAM NAME CHANGER\n')
    print(f'Steam account: ' + check_status_authorized() + '\n')
    print('1 - Start Program\n2 - Change Steam account\n3 - Change nicknames set\n4 - Reset "config.json" file\n'
          '5 - Exit program')
    user_choose = input('>>> ')
    if user_choose == '1':
        print(MENU_CHOICE_1)
    elif user_choose == '2':
        print(MENU_CHOICE_2)
    elif user_choose == '3':
        print(MENU_CHOICE_3)
    elif user_choose == '4':
        print(MENU_CHOICE_4)
    elif user_choose == '5':
        print(MENU_CHOICE_5)
    else:
        print(MENU_CHOICE_6)
        sys.exit()


def start():
    import ipdb; ipdb.set_trace() # BEFORE SETTINGS
    settings()
    import ipdb; ipdb.set_trace() # STATUS CHECKING
    if not check_status_authorized():
        if not steam_login():
            sys.exit()
    menu()


if __name__ == '__main__':
    start()
