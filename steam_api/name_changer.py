import random
import time

from selenium.webdriver.common.by import By

from response_handler import errors
from scripts import config_json_func as conf_json



# times = 0
# last_nickname = '.'
#
# def change_name_randomly(driver):
#     print('Changing started...')
#     while True:
#         try:
#             global times, last_nickname
#             input_line = driver.find_element(By.CLASS_NAME, 'DialogInput.DialogInputPlaceholder.DialogTextInputBase')
#             submit_btn = driver.find_element(By.CLASS_NAME, 'DialogButton._DialogLayout.Primary.Focusable')
#             nicknames_list = conf_json.getNickNamesSet()
#             nickname = ''
#             while not nickname == last_nickname:
#                 nickname = random.choice(nicknames_list)
#                 input_line.clear()
#                 input_line.send_keys(nickname)
#                 submit_btn.click()
#                 print(f'Successfully changed nickname - {nickname}')
#                 times += 1
#                 last_nickname = nickname
#                 print('Sleeping...')
#                 time.sleep(conf_json.getAutoChangeTime())
#                 change_name_randomly(driver)
#         except KeyboardInterrupt:
#             print('Exiting...')
#             raise
#         except Exception:
#             raise Exception(errors.while_changing_nickname())
#
#
#
# def change_name_ordinaly(driver):
#     print('Changing started...')
#     pass
#
#
# def change_name_develop(driver):
#     print('Changing started...')
#     pass
#
#
# def run_change_name(driver):
#     print('Starting changin name...')
#     change_type = conf_json.getAutoChangeType()
#     if change_type == 'random_list':
#         print(f'Change type - random list...')
#         change_name_randomly(driver)
#     if change_type == 'ordinal_list':
#         print(f'Change type - ordinal list')
#         change_name_ordinaly(driver)
#     print(f'Change type - developer')
#     change_name_develop(driver)

# while True:
#     print('Changing nickname...')
#     input_line.clear()
#     random_nickname = random.choice(nicknames_set)
#     if not random_nickname == last_nickname:
#         print(f'Random nickname is: {random_nickname}')
#         input_line.send_keys(random_nickname)
#         submit_btn.click()
#         last_nickname = random_nickname
#         print(f'Changed successfully\nSleeping {auto_change_time} sec.')
#         time.sleep(auto_change_time)


# while True:
#     times = times + 1
#     print('Changing nickname...')
#     input_line.send_keys('1')
#     submit_btn.click()
#     print(f'Random nickname SETTED, times {times}')
#     print(f'Changed successfully\nSleeping {auto_change_time} sec.')
#     time.sleep(auto_change_time)


# import time
# def abudabi():
#     try:
#         while True:
#             print('dasdas')
#             time.sleep(0.5)
#     except KeyboardInterrupt:
#         abc = int(input('enter value: '))
#         if abc == 1:
#             abudabi()
#     except Exception:
#         print('something go bad')
#     finally:
#         print('lol lol lol '
#
# abudabi()


#
# times = 0
# import time
#
# def change_name():
#     print('Changing nickname...')
#     last_nickname = ''
#     try:
#         while True:
#             global times
#             times += 1
#             print(f'printing times  {times}')
#             time.sleep(1)
#
#             # input_line = driver.find_element(By.CLASS_NAME, 'DialogInput.DialogInputPlaceholder.DialogTextInputBase')
#             # submit_btn = driver.find_element(By.CLASS_NAME, 'DialogButton._DialogLayout.Primary.Focusable')
#             # auto_change_time = conf_json.getAutoChangeTime()
#             #
#             # change_type = conf_json.getAutoChangeType()
#             # if change_type == 'random_list':
#             #     pass
#             # if change_type == 'ordinal_list':
#             #     pass
#
#             # Developer mode here
#     except KeyboardInterrupt:
#         input('dsada > ')
#         change_name()
#     except Exception:
#         print('Something go bad')
#     finally:
#         print('finall')
#
# change_name()
