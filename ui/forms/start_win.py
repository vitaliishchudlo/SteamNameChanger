from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.forms.statistic_win import StatisticWin
from ui.skeletons.start import Ui_StartWin


class StartWin(QtWidgets.QMainWindow, Ui_StartWin):
    def __init__(self, account_name):
        super().__init__()
        self.setupUi(self)

        self.account_name = account_name

        self.set_default_settings()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_start.clicked.connect(self.start)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

    def start(self):
        self.statistic_win = StatisticWin(self)
        self.statistic_win.show()
        self.hide()

    def set_default_settings(self):
        self.label_username.setText(self.account_name)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
