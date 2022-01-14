<<<<<<< HEAD
import os

from scripts import create_config_file, create_chrome_webdriver

from selenium import webdriver

from data import PLATFORM_RUNNING

=======
>>>>>>> e8fa894409b03ae5309175dfa6a8b1eecdcc8a7b
def files_manager():
    """
    Checks for the required script files.
    """
<<<<<<< HEAD
    # Create config file with all configurations of the program
    if not os.path.isfile('config.json'):
        create_config_file()

    #  Create chrome webdriver file
    if PLATFORM_RUNNING == 'Linux':
        if not os.path.isfile('chromedriver'):
            create_chrome_webdriver()
    else:
        if not os.path.isfile('chromedriver.exe'):
            create_chrome_webdriver()

    # return all logs here

def set_settings():
    """
    The function that is responsible for initialization the configurations from config file.
    """
    try:

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Clear some errors in the terminal

        # Option with hiding window

        #  Creating driver object and returning it
        driver = webdriver.Chrome(options=options)
        # ADD ALSO PATH TO WEBDRIVER

        return driver
    except Exception as error:
        print('Error')


def get_menu():
    """
     The function that is responsible for main menu of the program.
    """
    pass


=======
    pass


def set_settings():
    """
    The function that is responsible for initialization the configurations from config file.
    """
    pass


def get_menu():
    """
     The function that is responsible for main menu of the program.
    """
    pass


>>>>>>> e8fa894409b03ae5309175dfa6a8b1eecdcc8a7b
def app():
    """
    The main function, which responsible for starting the program and all managing it.
    """
    try:
        driver = files_manager()
        set_settings()
<<<<<<< HEAD
        get_menu()
    except Exception as err:
        print(f'[Error]: There were some errors when starting the program.\n[Reason]: {err}')
        os.remove('config.json')
=======

        get_menu()
    except Exception as err:
        print(f'[Error]: There were some errors when starting the program.\n[Reason]: {err}')
>>>>>>> e8fa894409b03ae5309175dfa6a8b1eecdcc8a7b


if __name__ == '__main__':
    app()
