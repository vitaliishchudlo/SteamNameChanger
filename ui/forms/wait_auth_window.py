from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

from ui.skeletons.wait_auth import Ui_WaitAuthWindow


class WaitAuthPopUp(QtWidgets.QMainWindow, Ui_WaitAuthWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.setupUi(self)

        self.prev = parent_window

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.btn_close.clicked.connect(self.close)

        self.label_gif.setMinimumSize(QtCore.QSize(25, 25))
        self.label_gif.setMaximumSize(QtCore.QSize(25, 25))
        self.label_gif.setScaledContents(True)

        self.loading = QMovie('ui/gifs/loading.gif')
        self.label_gif.setMovie(self.loading)

        self.startAnimation()

    def startAnimation(self):
        self.loading.start()

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def close(self):
        self.prev.setDisabled(False)
        self.hide()
