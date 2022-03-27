import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from ui.forms.wait_auth_window import WaitAuthPopUp
from ui.skeletons.auth import Ui_StartWindow


class StartWindow(QtWidgets.QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.center()

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.sign_in_btn.setDisabled(True)
        self.label_error.hide()

        self.refresh_combo_box()

        self.btn_hide.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())
        self.sign_in_btn.clicked.connect(self.authorize)

        self.combo_username.currentIndexChanged.connect(self.combo_check)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                self.setCursor(Qt.ArrowCursor)

        self.title_bar.mouseMoveEvent = moveWindow

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def authorize(self):
        self.setDisabled(True)
        self.waitauth_popup = WaitAuthPopUp(self)
        self.waitauth_popup.show()

    def combo_check(self):
        if self.combo_username.currentText() == '':
            return self.sign_in_btn.setDisabled(True)
        return self.sign_in_btn.setDisabled(False)

    def refresh_combo_box(self):
        pklfiles = []
        for file in os.listdir('web/cookies'):
            pklfiles.append(file)
        for pklfile in pklfiles:
            self.combo_username.addItem(pklfile)

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
