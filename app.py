import os
import sys
import time

from selenium import webdriver

from api_steam import authorize_user
from data import PLATFORM_RUNNING, MA_ENTER_PASSWORD, MA_ENTER_USERNAME, MA_CHOOSES
from response_handler import errors
from scripts import create_config_file, create_chrome_webdriver, hide_browser_window, \
    terminal, setSteamAccountPassword, setSteamAccountUsername, checkSteamAccountPassword, checkSteamAccountUsername, \
    checkNicknamesSetEmpty


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

    def menu(self):
        """
        The function which shall to manage the choices of the user and to run all the chosen functionality.
        """
        user_choice = ''
        user_choice = self.display_menu()
        # Start the program
        if user_choice == 1:
            terminal.clear()
            print('Starting the program...')
            # Check if it is existing account in the config.json
            if not checkSteamAccountUsername() or not checkSteamAccountPassword():
                terminal.display_sign_into_account_empty()
                self.menu()
            # Check if it is existing NickNamesSet in the config.json
            if not checkNicknamesSetEmpty():
                terminal.display_nicknames_set_empty()
                self.menu()
            print('Authorization...')
            # Trying to authorize
            authorize_user(self.driver)
            # if not authorize_user(self.driver):
            #     raise Exception(errors.authorizing_user())
            print('Authorization success')

            import ipdb; ipdb.set_trace()


        # Change nicknames set [UnWorkable now]
        elif user_choice == 2:
            pass
        # Manage SteamAccount
        elif user_choice == 3:
            self.manage_account()
        # Exit the program
        elif user_choice == 4:
            self.exit_program()
        else:
            self.menu()

    def manage_account(self):
        try:
            terminal.display_manage_account()
            print(*MA_CHOOSES)
            try:
                user_choice = int(input('>>> '))
                if user_choice == 1:
                    username = input(f'{MA_ENTER_USERNAME}')
                    setSteamAccountUsername(username)
                    password = input(f'{MA_ENTER_PASSWORD}')
                    setSteamAccountPassword(password)
                    terminal.display_success_account(username)
                    self.menu()
                elif user_choice == 2:
                    self.menu()
                else:
                    raise ValueError
            except ValueError:
                terminal.clear()
                print('Please enter a valid value')
                time.sleep(1.5)
                self.manage_account()
        except Exception as err:
            print(err)

    @staticmethod
    def exit_program():
        terminal.display_exit()
        sys.exit()


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
