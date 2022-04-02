import os
import sys
import threading
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.skeletons.auth import Ui_AuthWin
from web.driver.browser import Browser

login_page = 'https://store.steampowered.com/login/'
account_page = 'https://store.steampowered.com/account/'


class StartWindow(QtWidgets.QMainWindow, Ui_AuthWin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_auth_status = 'pending'
        self.username = ''

        self.center()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.sign_in_btn.setDisabled(True)
        self.label_error.setVisible(False)

        self.combo_box_refresh()

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: sys.exit(-1))

        self.sign_in_btn.clicked.connect(self.authentication)

        self.combo_username.currentIndexChanged.connect(self.combo_box_check)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

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
        pklfiles = []
        for file in os.listdir('web/cookies'):
            pklfiles.append(file[:-4])
        for pklfile in pklfiles:
            self.combo_username.addItem(pklfile)

    def label_error_settext(self, message):
        try:
            self.label_error.setText(message)
            self.label_error.setVisible(True)
        except Exception:
            return

    def sign_up(self):
        """
        Register a new account
        """
        self.browser = Browser()
        self.browser.get_steam()
        while self.browser.driver.current_url == 'https://store.steampowered.com/login/':
            print('[INFO]: Waiting authorization')
            time.sleep(1)
        print('[INFO]: Checking user account')
        if not self.browser.driver.current_url == 'https://store.steampowered.com/':
            print('[ERROR]: User entered not Steam web page')
            self.user_auth_status = 'failed'
            self.return_auth_window('You entered not Steam page')
            return False
        print('[INFO]: Trying to check that user is logged in')
        if not self.browser.auth_status():
            self.user_auth_status = 'failed'
            self.return_auth_window('You are not logged in')
            return False
        else:
            self.user_auth_status = 'success'
            self.browser.save_cookies()
            self.username = self.browser.get_account_name()
            self.browser.quit()
            return True

    def sign_in(self, account_name):
        """
        Sign in account that exists
        """
        self.browser = Browser(hide=True)
        self.browser.get_steam()
        self.browser.load_cookies(account_name)
        if not bool(self.browser.auth_status()):
            self.user_auth_status = 'failed'
            self.return_auth_window('Bad cookies')
            return False
        self.user_auth_status = 'success'
        self.browser.save_cookies()
        self.browser.quit()
        self.username = account_name
        return True

    def return_auth_window(self, error_message=None):
        if error_message:
            try:
                self.label_error.setText(error_message)
                self.label_error.setVisible(True)
            except Exception:
                return
        self.browser.quit()
        self.setDisabled(False)

    def start_auth_thread(self):
        if self.combo_username.currentText() == 'Add a new account...':
            self.browser_thread = threading.Thread(target=self.sign_up)
            self.browser_thread.start()
        else:
            account_name = self.combo_username.currentText()
            self.browser_thread = threading.Thread(
                target=self.sign_in, args=(account_name,))
            self.browser_thread.start()

        while self.user_auth_status == 'pending':
            time.sleep(1)
        if self.user_auth_status == 'success':
            self.label_error_settext('Successfully authorized')
            self.setDisabled(False)
            self.close()
            # call the next window

    def authentication(self):
        """
        Check if user choose 'Add new account' or 'Account name'
        """
        self.user_auth_status = 'pending'
        self.auth_thread = threading.Thread(target=self.start_auth_thread)
        self.auth_thread.start()

        self.setDisabled(True)
        self.label_error_settext('Loading...')
