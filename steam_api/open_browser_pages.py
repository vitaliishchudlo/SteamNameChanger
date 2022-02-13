from selenium.webdriver.common.by import By


def get_edit_page(driver):
    driver.get('https://store.steampowered.com/account/')
    steam_id = driver.find_element(By.CLASS_NAME, 'youraccount_steamid').text[10:]
    driver.get(f'https://steamcommunity.com/profiles/{steam_id}/edit/info/')
