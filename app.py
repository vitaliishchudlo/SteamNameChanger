import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='PATH')

driver.get('https://store.steampowered.com/login/')

time.sleep(3)

login_input_line = driver.find_element(By.NAME, 'username')
password_input_line = driver.find_element(By.NAME, 'password')

login_input_line.send_keys('LOGIN')
password_input_line.send_keys('PASSWORD')

time.sleep(1)

driver.find_element_by_css_selector('.btn_blue_steamui.btn_medium.login_btn').click()

STEAM_GUARD_CODE = input('Plase, input your steam guard code here: ').upper()
print('\n\n\n   YOUR STEAM GUARD CODE: ', STEAM_GUARD_CODE, '\n\n\n')
steam_guard_input_line = driver.find_element(By.ID, 'twofactorcode_entry')
steam_guard_input_line.send_keys(STEAM_GUARD_CODE)

time.sleep(1)

driver.find_element_by_xpath('//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]/div[1]').click()

time.sleep(3)

STEAM_PROFILE_LINK = 'https://steamcommunity.com/id/YOUID/'

driver.get(f'{STEAM_PROFILE_LINK}edit/info/')

time.sleep(3)

new_name_input_line = driver.find_element(By.NAME, 'personaName')

new_name_input_line.clear()
new_name_input_line.send_keys('ilonka')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="application_root"]/div[2]/div[2]/form/div[7]/button[1]').click()

time.sleep(10)
driver.close()
driver.quit()
