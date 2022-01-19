
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
