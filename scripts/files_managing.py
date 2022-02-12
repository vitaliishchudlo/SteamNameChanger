import json
from data import config

# Create config.json file
def create_config_file():
    with open('config.json', 'w') as file:
        file.write(config.CONFIG_STRUCTURE_DICT)




# Download chrome webdriver file
def create_chrome_webdriver(name_file):
    pass
