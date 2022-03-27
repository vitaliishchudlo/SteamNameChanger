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

# login_page = 'https://store.steampowered.com/login/'
#
# import pickle
# driver = selenium.webdriver.Firefox()
# # driver = selenium.webdriver.Chrome()
# driver.get(login_page)
#
# while driver.current_url == login_page:
#     time.sleep(0.5)
# pickle.dump(driver.get_cookies(), open("cookies/cookies.pkl", "wb"))
# driver.close()
#
# driver = selenium.webdriver.Firefox()
# driver.get(login_page)
# cookies = pickle.load(open("cookies/cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)
# driver.refresh()
# time.sleep(50)
