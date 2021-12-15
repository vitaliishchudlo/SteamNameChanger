import os

from selenium.webdriver.common.by import By

from data import USER_LOGIN, USER_PASSWORD, STEAM_AUTHORIZATION_PAGE


def authorize_user(driver):
    username_form_field = driver.find_element(By.NAME, 'username')
    password_form_field = driver.find_element(By.NAME, 'password')

    username_form_field.send_keys(USER_LOGIN)
    password_form_field.send_keys(USER_PASSWORD)

    driver.find_element(By.CSS_SELECTOR, '.btn_blue_steamui.btn_medium.login_btn').click()

    os.system('cls')

    if driver.current_url == STEAM_AUTHORIZATION_PAGE:
        return False
    return True
