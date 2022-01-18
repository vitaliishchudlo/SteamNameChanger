import os

from scripts import create_config_file, create_chrome_webdriver

from selenium import webdriver


from response_handler import errors

def files_manager():
    """
    Checks for the required script files.
    """
    # Create config file with all default configurations of the program
    if not os.path.isfile('config.json'):
        create_config_file()
    #  Create chrome webdriver file
    import ipdb; ipdb.set_trace()
    if not os.path.isfile('chromedriver'):
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
        print('error')



def get_menu():
    """
     The function that is responsible for main menu of the program.
    """
    pass


def app():
    """
    The main function, which responsible for starting the program and all managing it.
    """
    try:
        files_manager()
        set_settings()
        get_menu()
    except Exception:
        print('dsadaasda')


if __name__ == '__main__':

    app()

