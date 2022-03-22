from PyQt5 import QtWidgets

from .skeletons.clear import Ui_MainWindow


class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
