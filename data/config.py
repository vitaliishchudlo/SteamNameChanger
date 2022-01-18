
import platform
import os

# Name of the program
# Version of the program
# Author

# Platform the program running on
PLATFORM_RUNNING = platform.system()

# WebDriver
PATH_TO_WEBDRIVER = os.getcwd().replace('\\\\', '\\') + '\\chromedriver.exe'
PATH_TO_WEBDRIVER_LINUX = os.getcwd() + '/chromedriver'


# Links on pages:


# Menu chooses:


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
    }
}

# Menu choises
