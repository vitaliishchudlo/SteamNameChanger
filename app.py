import os

from selenium import webdriver

import data
from open_browser_pages import open_authorization_page
# from selenium.webdriver.common.by import By
from scripts import create_chrome_webdriver, create_config_file, hide_browser_window

from api_steam import authorize_user

# import random
# import re


def clear_files():
    os.remove('chromedriver.exe')
    os.remove('config.json')
    print('\n\nClearing files\nFiles deleted: "chromedriver.exe", "config.json"')


try:
    if not os.path.isfile('chromedriver.exe'):
        create_chrome_webdriver()

    create_config_file()

    # data.PATH_TO_WEBDRIVER - like: "D:\\Folder\\Projects\\Python\\SteamNameChanger"
    path_to_webdriver = data.PATH_TO_WEBDRIVER

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear some log in console

    hide_browser_window(options)

    driver = webdriver.Chrome(executable_path=path_to_webdriver, options=options)


except Exception as err:
    os.system('cls')
    clear_files()
    print(f'\n\n {err}')


def steam_login():
    try:
        open_authorization_page(driver)
        if not authorize_user(driver):
            raise Exception

    except Exception:
        print('Error when authorization in the SteamAccount')



def start():
    steam_login()


if __name__ == '__main__':
    start()
