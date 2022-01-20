import os
import sys
import time

from selenium import webdriver

from data import PLATFORM_RUNNING, MENU_CHOOSES
from response_handler import errors
from scripts import create_config_file, create_chrome_webdriver, hide_browser_window

from scripts import terminal


class Menu:
    def __init__(self, driver):
        self.driver = driver

    def display_menu(self):
        """
        Display the menu choices.
        """
        terminal.clear()
        terminal.display_header()
        terminal.display_user_info()
        terminal.display_footer()
        terminal.display_menu()
        try:
            user_choice = int(input('\n>>> '))
            return user_choice
        except ValueError:
            terminal.clear()
            print('Please enter a valid value')
            time.sleep(2.5)
            self.display_menu()
            # raise ValueError(errors.enteringInteger())




    def menu(self):
        """
        The function which shall to manage the choices of the user and to run all the chosen functionality.
        """
        user_choice = self.display_menu()

        # Start the program
        if user_choice == 1:
            pass
        # Change nicknames set
        elif user_choice == 2:
            pass
        # Manage SteamAccount
        elif user_choice == 3:
            pass
        # Exit the program
        elif user_choice == 4:
            terminal.display_exit()
            sys.exit()
        else:
            self.menu()


def files_manager():
    """
    Checks for the required script files.
    """
    # Create config file with all default configurations of the program
    if not os.path.isfile('config.json'):
        create_config_file()
    #  Create chrome webdriver file
    if PLATFORM_RUNNING == 'Linux':
        if not os.path.isfile('chromedriver'):
            create_chrome_webdriver('/chromedriver_linux64.zip')
    elif PLATFORM_RUNNING == 'Windows':
        if not os.path.isfile('chromedriver.exe'):
            create_chrome_webdriver('/chromedriver_win32.zip')
    else:
        raise Exception(errors.platformRunning())

    # return all logs here


def set_options():
    """
    The function that is responsible for initialization the configurations from config file.
    """
    try:
        options = webdriver.ChromeOptions()
        # Clear some errors in the terminal
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # Option with hiding window
        options = hide_browser_window(options)
        return options
    except Exception as error:
        print(error)


def create_webdriver(options):
    """
    Create an object of the WebDriver class. Return driver object.
    """
    try:
        # Creating driver object and returning it
        return webdriver.Chrome(options=options)
    except Exception:
        raise Exception(errors.creatingWebDriver())


def app():
    """
    The main function, which responsible for starting the program and all managing it.
    """
    try:
        files_manager()
        options = set_options()
        driver = create_webdriver(options)
        Menu(driver).menu()
    except Exception as error:
        print(f'{error}')


if __name__ == '__main__':
    app()
