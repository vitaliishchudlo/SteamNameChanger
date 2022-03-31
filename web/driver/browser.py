import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By

login_page = 'https://store.steampowered.com/login/'
account_page = 'https://store.steampowered.com/account/'


class Browser:
    def __init__(self, hide=False):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--no-startup-window')
        if hide:
            self.options.headless = True
        self.driver = webdriver.Firefox(options=self.options)
        self.driver.set_window_size(450, 650)

    def auth_status(self):
        try:
            self.driver.get(account_page)
            if bool(self.driver.find_element(By.CLASS_NAME, 'youraccount_steamid').text[10:]):
                return True
            return False
        except Exception:
            return False

    def refresh(self):
        self.driver.refresh()

    def get_steam(self):
        self.driver.get(login_page)

    def quit(self):
        self.driver.close()

    def load_cookies(self, account_name):
        cookies = pickle.load(open(f'web/cookies/{account_name}.pkl', 'rb'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def save_cookies(self):
        self.driver.get(account_page)
        account_name = self.driver.find_element(
            By.CLASS_NAME, 'pageheader.youraccount_pageheader').text
        account_name = account_name[account_name.find(' ') + 1:].lower()
        pickle.dump(self.driver.get_cookies(), open(
            f'web/cookies/{account_name}.pkl', 'wb'))
