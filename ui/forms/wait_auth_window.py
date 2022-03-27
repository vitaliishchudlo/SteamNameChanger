import pickle
import threading
import time

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from selenium.webdriver.common.by import By

from ui.skeletons.wait_auth import Ui_WaitAuthWindow
from web.driver.browser import Browser


class WaitAuthPopUp(QtWidgets.QMainWindow, Ui_WaitAuthWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.setupUi(self)
        self.center()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.parent_window = parent_window

        self.btn_close.clicked.connect(self.close)

        self.label_gif.setMinimumSize(QtCore.QSize(25, 25))
        self.label_gif.setMaximumSize(QtCore.QSize(25, 25))
        self.label_gif.setScaledContents(True)

        self.loading = QMovie('ui/gifs/loading.gif')
        self.label_gif.setMovie(self.loading)

        self.startAnimation()

        self.browser_thread = threading.Thread(target=self.check_authorization)
        self.browser_thread.start()

    def check_authorization(self):
        if not self.parent_window.combo_username.currentText() == 'Add a new account...':
            username = self.parent_window.combo_username.currentText()
            self.label_title_settext(
                f'Authorization in the {username} account...')
            self.browser = Browser(hide=False)
            self.browser.get_steam()
            cookies = pickle.load(open(f'web/cookies/{username}', 'rb'))
            for cookie in cookies:
                self.browser.driver.add_cookie(cookie)
            self.browser.refresh()

        else:
            self.browser = Browser()
            self.browser.get_steam()
            while self.browser.driver.current_url == 'https://store.steampowered.com/login/':
                print('Waiting authorization...')
                time.sleep(1)
            self.label_title_settext('Checking your account...')
            if not self.browser.driver.current_url == 'https://store.steampowered.com/':
                print('Entered other page')
                return self.close()
            print('Trying to check that u logged in')
            if self.browser.auth_status():
                self.label_title_settext('Successfully authorized')
                self.label_gif.setPixmap(
                    QtGui.QPixmap('ui/icons/custom/done.png'))
            else:
                self.label_title_settext('ERROR')
                self.label_gif.setPixmap(QtGui.QPixmap(
                    'ui/icons/custom/icons8-close.svg'))
                time.sleep(3)
                return self.close()
            account_name = self.browser.driver.find_element(
                By.CLASS_NAME, 'pageheader.youraccount_pageheader').text
            account_name = account_name[account_name.find(' ') + 1:].lower()
            pickle.dump(self.browser.driver.get_cookies(), open(
                f'web/cookies/{account_name}.pkl', 'wb'))
            self.close()

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

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def label_title_settext(self, message):
        self._translate = QtCore.QCoreApplication.translate
        self.label_title.setText(self._translate('WaitAuthWindow',
                                                 f"""<html><head/><body><p align=\"center\"><span style=\"
                                                 font-size:14pt; font-weight:600;\">{message}
                                                 </span></p></body></html>"""))
