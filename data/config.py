
import platform
import os

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


# Menu chooses:
MENU_CHOOSES = ['1. Start the program', '2. Change nicknames set [UNWORKABLE]', '3. Manage SteamAccount', '4. Exit the program',
                '\n\nSelect next action (enter the integer): \n']

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
    "chromeWindowSettings": {
        "hideWindow": False
    },
    "autoChangeTime": 60
}

# Menu choises
