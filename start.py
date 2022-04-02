import sys

from PyQt5 import QtWidgets

from ui.forms.auth_win import AuthWin


def run():
    app = QtWidgets.QApplication(sys.argv)
    start_window = AuthWin()
    start_window.show()
    while not start_window.isVisible():
        print('exited')
    app.exec()


if __name__ == '__main__':
    run()
