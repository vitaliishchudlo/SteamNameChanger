import os

from selenium.webdriver.common.by import By

from scripts import getSteamAccountUsername, getSteamAccountPassword

from data import AUTHORIZATION_LINK

import time
import sys








def steam_guard_auth(steam_guard_code, type_auth):
    # Mobile auth
    if steam_guard_code == 'mobile':
        pass
    # Email auth
    else:
        pass

    # try:
    #     # Mobile entering the SteamGuard code
    #     steam_guard_input_line = driver.find_element(By.ID, 'authcode')
    #     steam_guard_input_line.send_keys(STEAM_GUARD_CODE)
    #     print('Entering the mobile SteamGuard code')
    # except Exception:
    #     # Email entering the SteamGuard code
    #     steam_guard_input_line = driver.find_element(By.ID, 'authcode')
    #     steam_guard_input_line.send_keys(STEAM_GUARD_CODE)
    #     print('Entering the email SteamGuard code')

def check_type_auth(driver):
    try:
        # Mobile auth
        steam_guard_input_line = driver.find_element(By.ID, 'authcode')
        return 'mobile'
    except Exception:
        # Email auth
        steam_guard_input_line = driver.find_element(By.ID, 'authcode')
        return 'email'


def authorize_user(driver):
    driver.get(AUTHORIZATION_LINK)

    driver.find_element(By.NAME, 'username').send_keys(getSteamAccountUsername())
    driver.find_element(By.NAME, 'password').send_keys(getSteamAccountPassword())

    driver.find_element(By.CSS_SELECTOR, '.btn_blue_steamui.btn_medium.login_btn').click()
    time.sleep(0.5)

    # Check if the Steam login and password true
    try:
        driver.find_element(By.CLASS_NAME, 'newmodal')
        print('Username and password are good\n')
        STEAM_GUARD_CODE = input('Please, input your SteamGuard code:\n>>> ').upper()
        print('\n\nYOUR STEAM GUARD CODE: ', STEAM_GUARD_CODE, '\n\n')
        type_auth = check_type_auth(driver)
        try:
            steam_guard_auth(STEAM_GUARD_CODE, type_auth)
            return True
        except Exception:
            # raise guard error:
            pass
    except Exception:
        # raise error bad credentials
        pass

