from PyQt5.QtWidgets import *
from ui_view_member import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap


class ViewMember(QMainWindow, Ui_ViewMember):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        self.btn_show.released.connect(self.showClicked)

        @pyqtSlot()
        def closeClicked(self):
            self.close()

        @pyqtSlot()
        def saveClicked(self):
            print("save button clicked.")

        @pyqtSlot()
        def showClicked(self):
            self.showMemberInfo()
            print("show button clicked.")

        def showMemberInfo(self):
