import os
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie

from ui.forms.start_win import StartWin
from ui.skeletons.auth import Ui_AuthWin
from web.driver.browser import Browser


class AuthWin(QtWidgets.QMainWindow, Ui_AuthWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.account_name = ''

        self.center()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.sign_in_btn.setDisabled(True)
        self.label_error.setVisible(False)

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())
        self.sign_in_btn.clicked.connect(self.start_auth_worker)

        self.auth_worker = AuthWorker(self)
        self.auth_worker.AuthResult.connect(self.AuthResultSlot)

        self.combo_box_refresh()
        self.combo_username.currentIndexChanged.connect(self.combo_box_check)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

    def start_auth_worker(self):
        self.setDisabled(True)
        self.loading = QMovie('ui/gifs/loading.gif')
        self.label_error.setMovie(self.loading)
        self.label_error.setMinimumSize(QtCore.QSize(25, 25))
        self.label_error.setMaximumSize(QtCore.QSize(25, 25))
        self.label_error.setScaledContents(True)
        self.loading.start()
        self.label_error.setVisible(True)
        self.auth_worker.start()

    def AuthResultSlot(self, message):
        self.start_win = StartWin(message)
        self.start_win.show()
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def combo_box_check(self):
        if self.combo_username.currentText() == '':
            return self.sign_in_btn.setDisabled(True)
        return self.sign_in_btn.setDisabled(False)

    def combo_box_refresh(self):
        if not os.path.isdir('web'):
            os.mkdir('web')
        if not os.path.isdir('web/cookies'):
            os.mkdir('web/cookies')
        pklfiles = []
        for file in os.listdir('web/cookies'):
            pklfiles.append(file[:-4])
        for pklfile in pklfiles:
            self.combo_username.addItem(pklfile)

    def label_error_settext(self, message):
        try:
            self.label_error.setMinimumSize(QtCore.QSize(100, 30))
            self.label_error.setMaximumSize(QtCore.QSize(100, 30))
            self.label_error.setText(message)
            self.label_error.setVisible(True)
        except Exception:
            return


class AuthWorker(QThread):
    AuthResult = pyqtSignal(str)

    def __init__(self, parent_win):
        super().__init__()
        self.parent_win = parent_win
        self.account_name = ''

    def run(self):
        if self.parent_win.combo_username.currentText() == 'Add a new account...':
            if self.sign_up():
                return self.AuthResult.emit(self.account_name)
        else:
            account_name = self.parent_win.combo_username.currentText()
            if self.sign_in(account_name):
                return self.AuthResult.emit(self.account_name)

    def stop(self):
        self.quit()

    def sign_up(self):
        """
        Register a new account
        """
        self.browser = Browser(hide=False)
        self.browser.get_home()
        while self.browser.driver.current_url == 'https://steamcommunity.com/login/home/':
            time.sleep(0.5)
        if self.browser.driver.current_url.find('https://steamcommunity.com/id/') < 0:
            if self.browser.driver.current_url.find('https://steamcommunity.com/profiles/') < 0:
                self.return_auth_window('Do not leave Steam`s page')
                return False
        if not self.browser.auth_status():
            self.return_auth_window('You are not authorized')
            return False
        else:
            self.browser.save_cookies()
            self.account_name = self.browser.get_account_name()
            self.browser.quit()
            self.return_auth_window('Successfully authorized')
            return True

    def sign_in(self, account_name):
        """
        Sign in account that exists
        """
        self.browser = Browser()
        self.browser.load_cookies(account_name)
        if not bool(self.browser.auth_status()):
            self.return_auth_window('Bad cookies')
            return False
        self.browser.save_cookies()
        self.account_name = account_name
        self.browser.quit()
        return True

    def return_auth_window(self, error_message=None):
        if error_message:
            try:
                self.parent_win.label_error.setMinimumSize(
                    QtCore.QSize(250, 25))
                self.parent_win.label_error.setMaximumSize(
                    QtCore.QSize(250, 25))
                self.parent_win.label_error.setText(error_message)
                self.parent_win.label_error.setVisible(True)
                self.parent_win.setDisabled(False)
            except Exception:
                return
        self.browser.quit()
