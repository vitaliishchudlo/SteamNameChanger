from PyQt5 import QtWidgets

from ui.skeletons.start import Ui_StartWin


class MainWindow(QtWidgets.QMainWindow, Ui_StartWin):
    def __init__(self, browser):
        super().__init__()
        self.setupUi(self)
        # self.center()

        self.browser = browser

    #     self.setWindowFlags(Qt.FramelessWindowHint)
    #
    #     def moveWindow(event):
    #         if event.buttons() == Qt.LeftButton:
    #             self.move(self.pos() + event.globalPos() - self.dragPos)
    #             self.dragPos = event.globalPos()
    #             self.setCursor(Qt.ArrowCursor)
    #
    #     self.title_bar.mouseMoveEvent = moveWindow
    #
    # def mousePressEvent(self, event):
    #     self.dragPos = event.globalPos()
    #
    # def center(self):
    #     qr = self.frameGeometry()
    #     cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())
