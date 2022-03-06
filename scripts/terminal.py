import os
import shutil
import time

from data import PLATFORM_RUNNING, MENU_CHOOSES
from scripts import config_json_func as conf_json


def clear():
    if PLATFORM_RUNNING == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def get_columns_number():
    number_clm = shutil.get_terminal_size().columns
    return number_clm


def display_header():
    clm = get_columns_number()
    print('■ ' * (clm // 2))
    print('S T E A M   N A M E   C H A N G E R'.center(clm))
    print('v. 2.0    by Vitalii Shchudlo'.rjust(clm) + '(NightExpress)'.rjust(clm))
    print('■ ' * (clm // 2))
    # print('☁ ' * clm)


def display_user_info():
    clm = get_columns_number()
    username = conf_json.getSteamAccountUsername()
    nicknames_set = conf_json.getNickNamesSet()
    auto_change_time = conf_json.getAutoChangeTime()
    if not nicknames_set == 'N/A':
        nicknames_set = ", ".join(nicknames_set)
    print(
        f'Profile information:'.center(clm) +
        '\n' +
        f'   ● SteamAccount: {username}'.ljust(clm) +
        f'   ● Nicknames for change: {nicknames_set}'.ljust(clm) +
        f'   ● Auto change time: {auto_change_time} seconds\n'.ljust(clm)
    )


def display_footer():
    clm = get_columns_number()
    print(('. ' * (clm // 2)).center(clm))


def display_menu():
    clm = get_columns_number()
    print('Main menu:'.center(clm))
    print(*MENU_CHOOSES, sep='\n   ')


def display_exit():
    clear()
    clm = get_columns_number()
    print('B'.center(clm))
    clear()
    print('BY'.center(clm))
    clear()
    print('BYE'.center(clm))
    clear()
    print('BYE B'.center(clm))
    clear()
    print('BYE BY'.center(clm))
    clear()
    print('❤ BYE BYE ❤'.center(clm) + '❤❤❤❤❤❤❤'.center(clm - 4))
    time.sleep(1.5)


def display_manage_account():
    username = conf_json.getSteamAccountUsername()
    clear()
    display_header()
    print(f'Your Steam account is: {username}\n')
    display_footer()


def display_success_account(username):
    clear()
    clm = get_columns_number()
    print(f'You have successfully added {username} account'.center(clm))
    time.sleep(1.5)


def display_sign_into_account_empty():
    clear()
    clm = get_columns_number()
    print('The username or password is invalid'.center(clm) + 'Please, sign in to your Steam Account again'.center(clm))
    time.sleep(3)


def display_nicknames_set_empty():
    clear()
    clm = get_columns_number()
    print('Nicknames set is empty'.center(clm) + 'Please, create Nicknames set'.center(clm))
    time.sleep(1.5)


def get_steam_guard_code():
    pass
