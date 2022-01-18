import sys


def error_handler(func):
    def wrapper():
        print('[Error]: There were some errors when starting the program.')
        print(f'[Reason]: {func()}')
        sys.exit()
    return wrapper()
#
# @error_handler
def platformRunning():
    return 'The operating system is not presently supported to run this application'


# @error_handler
# def preparingFiles():
#         return 'An error occurred while preparing the required files'
#
#
# @error_handler
# def InternetConnection():
#     return 'Check your internet connection'
