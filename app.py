import sys

from PyQt5 import QtWidgets

from ui.forms.auth_win import AuthWin


def run():
    app = QtWidgets.QApplication(sys.argv)
    start_window = AuthWin()
    start_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
