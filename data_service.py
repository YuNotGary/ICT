# coding: utf-8
from PyQt5 import QtCore
from data_process import process

class ProcessService(QtCore.QThread):
    sig_result = QtCore.pyqtSignal(int, list)
        def __init__(self, parent):
            super().__init__(parent)

        def run(self) -> None: