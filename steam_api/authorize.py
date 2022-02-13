import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from data import AUTHORIZATION_LINK
from response_handler import errors
from scripts import config_json_func as conf_json
from scripts import terminal


def steam_guard_auth(driver, steam_guard_code, type_auth):
    # Mobile auth
    if type_auth == 'mobile':
        steam_guard_input_line = driver.find_element(By.ID, 'twofactorcode_entry')
        steam_guard_input_line.send_keys(steam_guard_code)
        steam_guard_input_line.send_keys(Keys.ENTER)
        # driver.find_element(By.CLASS_NAME, 'auth_button.leftbtn').click()
        time.sleep(2.2)
        if driver.current_url == 'https://store.steampowered.com/':
            return True
        raise Exception(errors.bad_steam_guard_code())
    # Email auth
    else:
        steam_guard_input_line = driver.find_element(By.ID, 'authcode')
        steam_guard_input_line.send_keys(steam_guard_code)
        steam_guard_input_line.send_keys(Keys.ENTER)
        # driver.find_element(By.CLASS_NAME, 'auth_button.leftbtn').click()
        time.sleep(2.2)
        try:
            driver.find_element(By.CLASS_NAME, 'auth_icon.auth_icon_unlock')
            return True
        except Exception:
            raise Exception(errors.bad_steam_guard_code())


def check_type_auth(driver):
    if driver.find_element(By.CLASS_NAME, 'login_modal.loginTwoFactorCodeModal').is_displayed():
        # Mobile phone code
        return 'mobile'
    else:
        # Email phone code
        driver.find_element(By.CLASS_NAME, 'login_modal.loginAuthCodeModal').is_displayed()
        return 'email'


def authorize_user(driver):
    driver.get(AUTHORIZATION_LINK)
    driver.find_element(By.NAME, 'username').send_keys(conf_json.getSteamAccountUsername())
    driver.find_element(By.NAME, 'password').send_keys(conf_json.getSteamAccountPassword())
    driver.find_element(By.CSS_SELECTOR, '.btn_blue_steamui.btn_medium.login_btn').click()
    time.sleep(2.2)

    # Check if the Steam login and password is correct
    try:
        driver.find_element(By.CLASS_NAME, 'newmodal')
        print('Username and password are correct\n')
        STEAM_GUARD_CODE = input('Please, input your SteamGuard code:\n>>> ').upper()
        print('\n\nYOUR STEAM GUARD CODE: ', STEAM_GUARD_CODE, '\n\n')
        type_auth = check_type_auth(driver)
        steam_guard_auth(driver, STEAM_GUARD_CODE, type_auth)
        return True
    except:
        terminal.clear()
        raise Exception(errors.bad_credentials())
