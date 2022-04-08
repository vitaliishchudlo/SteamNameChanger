import random
import time
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
from selenium.webdriver.common.by import By

from ui.skeletons.statistic import Ui_StatisticWindow
from web.driver.browser import Browser


class StatisticWin(QtWidgets.QMainWindow, Ui_StatisticWindow):
    def __init__(self, start_win):
        super().__init__()
        self.setupUi(self)

        self.browser = Browser()

        self.start_win = start_win
        self.label_username.setText(self.start_win.label_username.text())

        self.btn_stop.clicked.connect(self.return_back)

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(self.exit())

        self.changer_worker_status = True
        self.changer_worker = ChangeWorker(self)
        self.changer_worker.LogsUpdate.connect(self.LogsUpdate)
        self.changer_worker.start()

        self.setWindowFlags(Qt.FramelessWindowHint)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

    def exit(self):
        self.browser.quit()
        self.close()

    def return_back(self):
        self.changer_worker_status = False
        self.browser.quit()
        self.start_win.show()
        self.hide()

    def LogsUpdate(self, message):
        old_message = self.text_logs.toPlainText()
        new_message = old_message + message + '\n'
        self.text_logs.setText(new_message)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class ChangeWorker(QThread):
    LogsUpdate = pyqtSignal(str)

    def __init__(self, parent_win):
        super().__init__()
        self.parent_win = parent_win
        self.interval = int(self.parent_win.start_win.comboBox.currentText())
        if self.parent_win.start_win.ordinal.isChecked():
            self.type = 'ordinal'
        if self.parent_win.start_win.random.isChecked():
            self.type = 'random'
        self.counter_times = 0
        self.current_nickname = 'N/A'
        self.last_update = 'N/A'

    def ordinaly_change(self):
        self.parent_win.btn_stop.setDisabled(False)
        input_line = self.browser.driver.find_element(
            By.CLASS_NAME, 'DialogInput.DialogInputPlaceholder.DialogTextInputBase')
        submit_btn = self.browser.driver.find_element(
            By.CLASS_NAME, 'DialogButton._DialogLayout.Primary.Focusable')
        while self.parent_win.changer_worker_status:
            try:
                for future_nickname in self.nicknames_set:
                    self.current_nickname = future_nickname
                    self.counter_times += 1
                    self.last_update = datetime.strftime(
                        datetime.now(), '%X %x')

                    input_line.clear()
                    input_line.send_keys(self.current_nickname)
                    submit_btn.click()

                    self.parent_win.value_current_nick.setText(
                        self.current_nickname)
                    self.parent_win.value_counter.setText(
                        str(self.counter_times))
                    self.parent_win.value_last.setText(self.last_update)

                    self.LogsUpdate.emit(
                        '[INFO] Nickname setted!')
                    self.LogsUpdate.emit(
                        f'[INFO] Sleeping for {self.interval}')
                    time.sleep(self.interval)

            except Exception as err:
                return self.LogsUpdate.emit(
                    f'[ERROR]: {err}')

    def random_change(self):
        self.parent_win.btn_stop.setDisabled(False)
        while self.parent_win.changer_worker_status:
            try:
                input_line = self.browser.driver.find_element(
                    By.CLASS_NAME, 'DialogInput.DialogInputPlaceholder.DialogTextInputBase')
                submit_btn = self.browser.driver.find_element(
                    By.CLASS_NAME, 'DialogButton._DialogLayout.Primary.Focusable')
                future_nickname = random.choice(self.nicknames_set)
                while not future_nickname == self.current_nickname:
                    self.current_nickname = future_nickname
                    self.counter_times += 1
                    self.last_update = datetime.strftime(
                        datetime.now(), '%X %x')
                    input_line.clear()
                    input_line.send_keys(self.current_nickname)
                    submit_btn.click()

                    self.parent_win.value_current_nick.setText(
                        self.current_nickname)
                    self.parent_win.value_counter.setText(
                        str(self.counter_times))
                    self.parent_win.value_last.setText(self.last_update)

                    self.LogsUpdate.emit(
                        '[INFO] Nickname setted!')
                    self.LogsUpdate.emit(
                        f'[INFO] Sleeping for {self.interval}')
                    time.sleep(self.interval)
            except Exception as err:
                print(err)
                return self.LogsUpdate.emit(
                    f'[ERROR]: {err}')

    def run(self):
        self.parent_win.btn_stop.setDisabled(True)
        self.nicknames_update()
        self.LogsUpdate.emit('[INFO]: Starting changing...')
        self.browser = self.parent_win.browser
        self.browser.load_cookies(self.parent_win.label_username.text())
        self.browser.get_edit_page()
        if self.parent_win.start_win.ordinal.isChecked():
            self.ordinaly_change()
        if self.parent_win.start_win.random.isChecked():
            self.random_change()

    def stop(self):
        pass

    def nicknames_update(self):
        try:
            self.nicknames_set = self.parent_win.start_win.nicknames_list.toPlainText()
            self.nicknames_set = self.nicknames_set.replace(
                '\n', '').replace(' ', '')
            if len(self.nicknames_set) < 4:
                return self.LogsUpdate.emit(
                    '[ERROR]: Nicknames set must consist of at least two nicknames')
            self.nicknames_set = self.nicknames_set.split(',')
            self.LogsUpdate.emit(
                f'[INFO]: Nicknames set successfully loaded: {", ".join(self.nicknames_set)}')
            self.LogsUpdate.emit(
                f'[INFO]: Interval: {self.interval} seconds')
            self.LogsUpdate.emit(
                f'[INFO]: Type of changing: {self.type}')

        except Exception:
            self.LogsUpdate.emit(
                '[ERROR]: Can`t load nicknames set. The default set are: Example 1, Example 2, Example 3')
