import json
import os
import zipfile

import requests
import wget

from data import config
from response_handler import errors


# Create config.json file
def create_config_file():

    with open('config.json', 'w') as file:
        file.write(json.dumps(config.CONFIG_STRUCTURE_DICT, indent=4))


# Download chrome webdriver file
def create_chrome_webdriver(file_type):
    try:
        # Get the latest GoogleChrome driver version number
        version = requests.get(config.CHROMEDRIVER_VERSION_LINK).text
        # Define the OS and build a download link for it
        chromedriver_link = f'https://chromedriver.storage.googleapis.com/{version}{file_type}'
        # download the zip file using the url built above
        latest_driver_zip = wget.download(chromedriver_link)
        # extract the zip file
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall()
        os.remove(latest_driver_zip)

    except ConnectionError:
        raise ConnectionError(errors.internetConnection())

    except Exception:
        raise FileExistsError(errors.preparingFiles())
