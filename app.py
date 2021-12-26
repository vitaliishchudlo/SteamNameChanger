def files_manager():
    """
    Checks for the required script files.
    """
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


def app():
    """
    The main function, which responsible for starting the program and all managing it.
    """
    try:
        set_settings()

        get_menu()
    except Exception as err:
        print(f'[Error]: There were some errors when starting the program.\n[Reason]: {err}')


if __name__ == '__main__':
    app()
