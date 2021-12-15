from data import STEAM_AUTHORIZATION_PAGE


def open_authorization_page(driver):
    try:
        return driver.get(STEAM_AUTHORIZATION_PAGE)
    except Exception as err:
        print(f'\nError with opening SteamPage:\n   {err}')
