import os
import threading
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from selenium.webdriver.common.by import By

from ui.forms.main_window import MainWindow
from ui.skeletons.auth import Ui_StartWindow
from web.driver.browser import Browser

login_page = 'https://store.steampowered.com/login/'
account_page = 'https://store.steampowered.com/account/'


class StartWindow(QtWidgets.QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user_auth_status = 'pending'

        self.center()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.sign_in_btn.setDisabled(True)
        self.label_error.setVisible(False)

        self.combo_box_refresh()

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())
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
            return
        print('[INFO]: Trying to check that user is logged in')
        if not self.browser.auth_status():
            self.user_auth_status = 'failed'
            self.return_auth_window('You are not logged in')
            return
        else:
            self.label_error_settext('Successfully authorized')
            self.user_auth_status = 'success'
            self.browser.save_cookies()
            return

    def sign_in(self, account_name):
        """
        Sign in account that exists
        """
        self.browser = Browser(hide=True)
        self.browser.get_steam()
        self.browser.load_cookies(account_name)
        if not bool(self.browser.auth_status()):
            self.user_auth_status = 'failed'
            return
        self.user_auth_status = 'success'
        self.browser.save_cookies()
        return

    def start_authentication_thread(self, sign_in=None, account_name=None, sign_up=None):
        if sign_in:
            self.browser_thread = threading.Thread(
                target=self.sign_in, args=(account_name,))
            self.browser_thread.start()
        if sign_up:
            self.browser_thread = threading.Thread(target=self.sign_up)
            self.browser_thread.start()

        while self.user_auth_status == 'pending':
            time.sleep(1)
        if self.user_auth_status == 'success':
            return True
        return False

    def authentication(self):
        """
        Check if user choose 'Add new account' or 'Account name'
        """
        # Sign up

        if self.isActiveWindow():
            self.setVisible(False)

        if self.combo_username.currentText() == 'Add a new account...':
            if not self.start_authentication_thread(sign_up=True):
                self.setVisible(True)
                return self.label_error.setText('Can`t sign up')

            self.browser.driver.get(account_page)
            account_name = self.driver.find_element(
                By.CLASS_NAME, 'pageheader.youraccount_pageheader').text
            account_name = account_name[account_name.find(' ') + 1:].lower()
            self.browser.quit()
            self.browser = Browser(hide=True)
            self.browser.get_steam()
            self.browser.load_cookies(account_name)
            # Next page
        # Sign in
        else:
            account_name = self.combo_username.currentText()
            if not self.start_authentication_thread(sign_in=True, account_name=account_name):
                self.setVisible(True)
                self.label_error_settext(
                    f'Can`t sign in to {account_name}. Time expired')
                return
        self.main_window = MainWindow(account_name)
        self.main_window.show()
        self.close()

    def label_error_settext(self, message):
        try:
            self.label_error.setText(message)
            self.label_error.setVisible(True)
        except Exception:
            return

    def return_auth_window(self, error_message=None):
        if error_message:
            try:
                self.label_error.setText(error_message)
                self.label_error.setVisible(True)
            except Exception:
                return
        self.browser.quit()
        self.setDisabled(False)

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

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
