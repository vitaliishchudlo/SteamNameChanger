from PyQt5 import QtWidgets

from ui.skeletons.statistic import Ui_StatisticWindow


class StatisticWin(QtWidgets.QMainWindow, Ui_StatisticWindow):
    def __init__(self, parent_win):
        super().__init__()
        self.setupUi(self)

        self.parent_win = parent_win

        self.btn_stop.clicked.connect(self.return_back)

    def return_back(self):
        self.parent_win.show()
        self.hide()
