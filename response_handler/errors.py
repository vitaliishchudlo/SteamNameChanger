def error_handler(func):
    def wrapper():
        return "[Error]: There were some errors when starting the program\n" \
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