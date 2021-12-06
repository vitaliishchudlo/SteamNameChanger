import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

path_to_webdriver = os.getcwd().replace('\\\\', '\\') + '\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=path_to_webdriver)

nicknames_for_change = []

last_nickname = ''




def steam_loging():
    driver.get('https://store.steampowered.com/login/')
    time.sleep(3)

    login_input_line = driver.find_element(By.NAME, 'username')
    password_input_line = driver.find_element(By.NAME, 'password')

    login_input_line.send_keys(input('Enter your steam login: '))
    password_input_line.send_keys(input('Enter your steam password: '))

    time.sleep(1)

    driver.find_element_by_css_selector('.btn_blue_steamui.btn_medium.login_btn').click()

    STEAM_GUARD_CODE = input('Please, input your steam guard code here: ').upper()

    print('\n\n\n   YOUR STEAM GUARD CODE: ', STEAM_GUARD_CODE, '\n\n\n')

    steam_guard_input_line = driver.find_element(By.ID, 'twofactorcode_entry')
    steam_guard_input_line.send_keys(STEAM_GUARD_CODE)

    driver.find_element_by_xpath('//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]/div[1]').click()

    time.sleep(3)


def get_steam_editprofile_page():
    STEAM_PROFILE_LINK = input('Enter your profile link: ')  
    driver.get(f'{STEAM_PROFILE_LINK}edit/info/')

    time.sleep(3)


def get_nicknames_from_user():
    choice = input(f'Your list with nicknames: {nicknames_for_change}\n Your want add more?\n\n1 - Yes\n2 - No\n>>> ')
    if choice == '1':
        new_nickname = input('Enter nickname: ')
        nicknames_for_change.append(new_nickname)
        get_nicknames_from_user()


def chose_nickname():
    global last_nickname

    nickname = random.choice(nicknames_for_change)
    if nickname == last_nickname:
        chose_nickname()
    last_nickname = nickname
    return nickname



def change_steam_name():
    new_name_input_line = driver.find_element(By.NAME, 'personaName')
    new_name_input_line.clear()
    nickname = chose_nickname()

    new_name_input_line.send_keys(nickname)

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="application_root"]/div[2]/div[2]/form/div[7]/button[1]').click()

    time.sleep(31)
    change_steam_name()


def start():
    steam_loging()
    get_steam_editprofile_page()
    get_nicknames_from_user()
    change_steam_name()


start()

driver.close()
driver.quit()
