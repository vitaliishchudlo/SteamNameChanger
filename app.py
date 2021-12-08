import os
import random
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import config

path_to_webdriver = os.getcwd().replace('\\\\', '\\') + '\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=path_to_webdriver)

nicknames_for_change = []


def steam_loging():
    driver.get('https://store.steampowered.com/login/')
    time.sleep(3)

    login_input_line = driver.find_element(By.NAME, 'username')
    password_input_line = driver.find_element(By.NAME, 'password')

    login_input_line.send_keys(config.USERNAME)
    password_input_line.send_keys(config.PASSWORD)

    driver.find_element(By.CSS_SELECTOR, '.btn_blue_steamui.btn_medium.login_btn').click()

    STEAM_GUARD_CODE = input('Please, input your steam guard code here: ').upper()

    print('\n\n\n   YOUR STEAM GUARD CODE: ', STEAM_GUARD_CODE, '\n\n\n')

    steam_guard_input_line = driver.find_element(By.ID, 'twofactorcode_entry')
    steam_guard_input_line.send_keys(STEAM_GUARD_CODE)

    driver.find_element(By.XPATH, '//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]').click()

    time.sleep(3)


def get_steam_editprofile_page():
    driver.get('https://store.steampowered.com/account/')
    ACCOUNT_STEAM_ID = driver.find_element(By.CLASS_NAME, 'youraccount_steamid').text
    ACCOUNT_STEAM_ID = re.sub('\D', '', ACCOUNT_STEAM_ID)
    driver.get(f'https://steamcommunity.com/profiles/{ACCOUNT_STEAM_ID}/edit/info/')


def get_nicknames_from_user():
    choice = input(f'Your list with nicknames: {nicknames_for_change}\n Your want add more?\n\n1 - Yes\n2 - No\n>>> ')
    if choice == '1':
        new_nickname = input('Enter nickname: ')
        nicknames_for_change.append(new_nickname)
        get_nicknames_from_user()


def save_last_nickname(last_nickname):
    config.LAST_NICK_NAME = last_nickname


def wait_for_120seconds():
    print('Time LEFT 120')
    time.sleep(60)
    print('Time LEFT 60')
    time.sleep(30)
    print('Time LEFT 31')
    time.sleep(6)
    print('Time LEFT 25')
    time.sleep(5)
    print('Time LEFT 20')
    time.sleep(5)
    print('Time LEFT 15')
    time.sleep(5)
    print('Time LEFT 10')
    time.sleep(5)
    print('Time LEFT 5')
    time.sleep(5)
    print('Time LEFT 1')


def change_steam_name():
    driver.refresh()
    time.sleep(2)
    new_name_input_line = driver.find_element(By.NAME, 'personaName')
    new_name_input_line.clear()
    nickname = random.choice(nicknames_for_change)

    if nickname == config.LAST_NICK_NAME:
        change_steam_name()
    save_last_nickname(nickname)

    new_name_input_line.send_keys(nickname)

    driver.find_element(By.XPATH, '//*[@id="application_root"]/div[2]/div[2]/form/div[7]/button[1]').click()

    print(f'Nickname was successfully update. Now your new nickname: {nickname}')

    wait_for_120seconds()

    change_steam_name()


def start():
    steam_loging()
    get_steam_editprofile_page()
    get_nicknames_from_user()
    change_steam_name()


start()

driver.close()
driver.quit()
