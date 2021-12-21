
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')


def files_manager():
    """
    Checks for the required script files.

    :return:
    """

    pass


def set_settings():
    print(os.getenv('First'))
    print(os.getenv('Second'))
    print(os.getenv('Login'))
    print(os.getenv('Password'))
    os.putenv('Login', 'My')
    print(os.getenv('Login'))










def app():
    try:
        set_settings()
    except Exception as err:
        print(f'[Error]: Some trouble with program. We can`t start it.\n[{err}]')






if __name__ == '__main__':
    app()
