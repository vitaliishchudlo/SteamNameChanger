import os
import platform

# Name of the program
# Version of the program
# Author

# Platform the program running on
PLATFORM_RUNNING = platform.system()

# Path to WebDriver
if PLATFORM_RUNNING == 'Linux':
    PATH_TO_WEBDRIVER = os.getcwd() + '/chromedriver'
elif PLATFORM_RUNNING == 'Windows':
    PATH_TO_WEBDRIVER = os.getcwd().replace('\\\\', '\\') + '\\chromedriver.exe'
else:
    PATH_TO_WEBDRIVER = None

# Links on pages:
CHROMEDRIVER_VERSION_LINK = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
GET_STEAM_ID_LINK = 'https://store.steampowered.com/account/'
STEAM_PROFILE_LINK = 'https://steamcommunity.com/profiles/'
AUTHORIZATION_LINK = 'https://store.steampowered.com/login/'

# Menu chooses:

MENU_CHOOSES = ['   1. Start the program', '2. Change nicknames set [UNWORKABLE]', '3. Manage SteamAccount',
                '4. Exit the program',
                '\n\n Select an action (1-4): \n']

MA_CHOOSES = ['1. Sign in to the new Steam account\n2. Return to the main menu\n\n']
MA_ENTER_USERNAME = 'Enter the username: \n>>> '
MA_ENTER_PASSWORD = 'Enter the password: \n>>> '

# Config.json file
CONFIG_STRUCTURE_DICT = {
    "userdata": {
        "username": "",
        "password": ""
    },
    "nickNamesManagement": {
        "nickNamesForChange": [],
        "lastNickName": None
    },
    "autoChangeTime": 60,
    "autoChangeType": "developer",
    "_autoChangeType": "random_list",
    "__autoChangeType": "ordinal_list",
    "chromeWindowSettings": {
        "hideWindow": True
    },
}
