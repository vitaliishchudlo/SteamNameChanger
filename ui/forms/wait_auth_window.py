from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

from ui.skeletons.wait_auth import Ui_WaitAuthWindow
from web.driver.browser import Browser


class WaitAuthPopUp(QtWidgets.QMainWindow, Ui_WaitAuthWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent_window = parent_window

        self.btn_close.clicked.connect(self.close)

        self.label_gif.setMinimumSize(QtCore.QSize(25, 25))
        self.label_gif.setMaximumSize(QtCore.QSize(25, 25))
        self.label_gif.setScaledContents(True)

        self.loading = QMovie('ui/gifs/loading.gif')
        self.label_gif.setMovie(self.loading)

        self.startAnimation()

        self.check_authorization()

        # self.browser = Browser()
        # self.browser_thread = threading.Thread(target=self.browser.get_steam)
        # self.browser_thread.start()

    def check_authorization(self):
        if not self.parent_window.combo_username.currentText() == 'Add a new account...':
            # Logging into chooses account
            pass
        else:
            self.browser = Browser()
            self.browser.get_steam()
            # Logging into a new account
            pass

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
        self.browser.quit()
        self.parent_window.setDisabled(False)
        self.hide()
