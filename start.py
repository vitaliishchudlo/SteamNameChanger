import sys

from PyQt5 import QtWidgets

from ui.clear import StartWindow


def run():
    app = QtWidgets.QApplication(sys.argv)
    start_window = StartWindow()
    start_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
