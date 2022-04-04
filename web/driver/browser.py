import os
import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW

login_page = 'https://store.steampowered.com/login/'
account_page = 'https://store.steampowered.com/account/'
home_page = 'https://steamcommunity.com/login/home/'


class Browser:
    def __init__(self, hide=True):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        self.service = Service('chromedriver.exe')
        self.service.creationflags = CREATE_NO_WINDOW
        if hide:
            self.options.headless = True
        self.driver = webdriver.Chrome(
            options=self.options, service=self.service)  # , service_log_path = os.devnull
        self.driver.set_window_size(450, 650)

    def auth_status(self):
        try:
            self.driver.get(home_page)
            if not bool(self.driver.current_url == home_page):
                return True
            return False
        except Exception:
            return False

    def refresh(self):
        self.driver.refresh()

    def get_steam(self):
        self.driver.get(login_page)

    def get_home(self):
        self.driver.get(home_page)

    def quit(self):
        self.driver.close()

    def cookies_folder_check(self):
        if not os.path.isdir('web'):
            os.mkdir('web')
        if not os.path.isdir('web/cookies'):
            os.mkdir('web/cookies')

    def load_cookies(self, account_name):
        self.cookies_folder_check()
        self.driver.get(home_page)
        cookies = pickle.load(open(f'web/cookies/{account_name}.pkl', 'rb'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def save_cookies(self):
        self.cookies_folder_check()
        account_name = self.get_account_name()
        # self.driver.get(home_page)
        pickle.dump(self.driver.get_cookies(), open(
            f'web/cookies/{account_name}.pkl', 'wb'))

    def get_account_name(self):
        self.driver.get(home_page)
        self.driver.set_window_size(1000, 500)
        self.driver.find_element(
            By.XPATH, '//*[@id="account_pulldown"]').click()
        account_name = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[3]/div/a[3]/span').text
        return account_name

    def get_edit_page(self):
        self.driver.get(f'{self.driver.current_url}/edit/info')


test = Browser()
test.cookies_folder_check()
