import random
import time

from selenium.webdriver.common.by import By

from response_handler import errors
from scripts import config_json_func as conf_json

times = 0
last_nickname = '.'


def change_name_randomly(driver):
    print('Changing started...')
    while True:
        try:
            global times, last_nickname
            input_line = driver.find_element(By.CLASS_NAME, 'DialogInput.DialogInputPlaceholder.DialogTextInputBase')
            submit_btn = driver.find_element(By.CLASS_NAME, 'DialogButton._DialogLayout.Primary.Focusable')
            nicknames_list = conf_json.getNickNamesSet()
            nickname = random.choice(nicknames_list)
            print(nickname)
            while not nickname == last_nickname:
                input_line.clear()
                input_line.send_keys(nickname)
                submit_btn.click()
                print(f'Successfully changed nickname - {nickname}')
                times += 1
                last_nickname = nickname
                print('Sleeping...')
                time.sleep(conf_json.getAutoChangeTime())
                # change_name_randomly(driver)
        except KeyboardInterrupt:
            print('Stopping the changing name...')
            time.sleep(3)
        except Exception:
            raise Exception(errors.while_changing_nickname())


def change_name_ordinaly(driver):
    print('Changing started...')
    pass


def change_name_develop(driver):
    print('Changing started...')
    pass


def run_change_name(driver):
    print('Starting changin name...')
    change_type = conf_json.getAutoChangeType()
    if change_type == 'random_list':
        print(f'Change type - random list...')
        change_name_randomly(driver)
    if change_type == 'ordinal_list':
        print(f'Change type - ordinal list')
        change_name_ordinaly(driver)
    if change_type == 'developer':
        print(f'Change type - developer')
        change_name_develop(driver)
    print('Going main menu')
