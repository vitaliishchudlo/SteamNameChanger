import time

from selenium.webdriver.common.by import By
from scripts import config_json_func as conf_json
import random

def change_name(driver):
    input_line = driver.find_element(By.CLASS_NAME, 'DialogInput.DialogInputPlaceholder.DialogTextInputBase')
    submit_btn = driver.find_element(By.CLASS_NAME, 'DialogButton._DialogLayout.Primary.Focusable')
    nicknames_set = conf_json.getNickNamesSet()
    auto_change_time = conf_json.getAutoChangeTime()
    last_nickname = ''
    while True:
        print('Changing nickname...')
        input_line.clear()
        random_nickname = random.choice(nicknames_set)
        if not random_nickname == last_nickname:
            print(f'Random nickname is: {random_nickname}')
            input_line.send_keys(random_nickname)
            submit_btn.click()
            last_nickname = random_nickname
            print(f'Changed successfully\nSleeping {auto_change_time} sec.')
            time.sleep(auto_change_time)









