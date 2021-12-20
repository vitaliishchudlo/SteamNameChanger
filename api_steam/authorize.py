import os

from selenium.webdriver.common.by import By

from data import STEAM_AUTHORIZATION_PAGE, get_user_login, get_user_password

import time
import sys


def authorize_user(driver):
    username_form_field = driver.find_element(By.NAME, 'username')
    password_form_field = driver.find_element(By.NAME, 'password')

    username_form_field.send_keys(get_user_login())
    password_form_field.send_keys(get_user_password())

    driver.find_element(By.CSS_SELECTOR, '.btn_blue_steamui.btn_medium.login_btn').click()

    os.system('cls')
    time.sleep(3)
    # НИЩЕ ПЕРЕВІРКА ЧИ ТРУ ДАНІ ДЛЯ ВХОДУ
    if driver.find_element(By.CLASS_NAME, 'newmodal'):
        STEAM_GUARD_CODE = input('Please, input your steam guard code here: ').upper()
        print('\n\n\n   YOUR STEAM GUARD CODE: ', STEAM_GUARD_CODE, '\n\n\n')

        try:
            # Mobile (SteamGuard) authorizing
            steam_guard_input_line = driver.find_element(By.ID, 'twofactorcode_entry')
            steam_guard_input_line.send_keys(STEAM_GUARD_CODE)
            print('twofactorcode_entry - mobile login')

        except Exception:
            # Email authorizing
            steam_guard_input_line = driver.find_element(By.ID, 'authcode')
            steam_guard_input_line.send_keys(STEAM_GUARD_CODE)
            print('authcode - email login')
        import ipdb; ipdb.set_trace()
        try:
            # Mobile (SteamGuard) authorizing
            driver.find_element(By.XPATH, '//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]').click()
            time.sleep(1.33)
            if driver.current_url == 'https://store.steampowered.com/':
                return True
            return False

        except Exception:
            # Email authorizing
            driver.find_element(By.XPATH, '//*[@id="auth_buttonset_entercode"]/div[1]').click()
            time.sleep(1.33)
            import ipdb;ipdb.set_trace()
            try:
                if driver.find_element(By.CLASS_NAME, 'auth_icon.auth_icon_unlock'):
                    return True
            except Exception:
                return False



    return print('bad authorization data')
