def error_handler(func):
    def wrapper():
        return "[Error]: There were some errors while the program was running\n" \
               f"[Reason]: {func()}"

    return wrapper


@error_handler
def platformRunning():
    return 'The operating system is not presently supported to run this application'


@error_handler
def preparingFiles():
    return 'An error occurred while preparing the required files'


@error_handler
def internetConnection():
    return 'Check your internet connection'


@error_handler
def creatingWebDriver():
    return 'An error occurred while creating the WebDriver window'


@error_handler
def enteringInteger():
    return 'Please enter a valid value'


@error_handler
def readingConfigJsonFile():
    return f'An error occurred while opening the "config.json" file'


@error_handler
def writingConfigJsonFile():
    return f'An error occurred while writing the "config.json" file'


@error_handler
def authorizing_user():
    return f'Bad authorization'


@error_handler
def bad_credentials():
    return f'Your username or password is incorrect'


@error_handler
def bad_steam_guard_code():
    return 'Your SteamGuard code is incorrect'
