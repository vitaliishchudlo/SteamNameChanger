from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from ui.skeletons.statistic import Ui_StatisticWindow


class StatisticWin(QtWidgets.QMainWindow, Ui_StatisticWindow):
    def __init__(self, start_win):
        super().__init__()
        self.setupUi(self)

        self.start_win = start_win

        self.btn_stop.clicked.connect(self.return_back)

        self.changer_worker = ChangeWorker(self)
        self.changer_worker.LogsUpdate.connect(self.LogsUpdate)
        self.changer_worker.start()

    def return_back(self):
        self.start_win.show()
        self.hide()

    def LogsUpdate(self, message):
        old_message = self.text_logs.toPlainText()
        new_message = old_message + message + '\n'
        self.text_logs.setText(new_message)


class ChangeWorker(QThread):
    # CurrentNickname = pyqtSignal(str)
    # CounterTimes = pyqtSignal(int)
    # LastUpdate = pyqtSignal()
    LogsUpdate = pyqtSignal(str)

    def __init__(self, parent_win):
        super().__init__()
        self.parent_win = parent_win
        self.interval = self.parent_win.start_win.comboBox.currentText()
        if self.parent_win.start_win.ordinal.isChecked():
            self.type = 'ordinal'
        if self.parent_win.start_win.random.isChecked():
            self.type = 'random'
        self.value_counter = self.parent_win.value_counter.text()
        self.current_nickname = self.parent_win.value_current_nick.text()
        self.last_update = self.parent_win.value_last.text()

    def run(self):
        self.nicknames_update()

    def nicknames_update(self):
        try:
            self.nicknames_set = self.parent_win.start_win.nicknames_list.toPlainText()
            self.nicknames_set = self.nicknames_set.replace(
                '\n', '').replace(' ', '')
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

    def stop(self):
        pass
