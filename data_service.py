# coding: utf-8
from PyQt5 import QtCore
from data_process import process

class ProcessService(QtCore.QThread):
    #  result Signal with two parameters (integer, list)
    sig_result = QtCore.pyqtSignal(int, list)
    #  error Signal with two parameters (integer, str)
    sig_error = QtCore.pyqtSignal(int, str)
    #  msg #  result Signal with two parameters (integer, str)
    sig_msg = QtCore.pyqtSignal(int, str)

    def __init__(self, parent):
        super().__init__(parent)

        self.tasks = []

    def reload(self, tasks):
        """Incoming task list"""
        self.tasks = tasks

    def run(self) -> None:
        # Get the number to be processed
        num = len(self.tasks)
        # Loop every task
        for index in range(num):
            # Get the value of fp and shift
            fp, shift = self.tasks[index]
            try:
                # Call the function to process the result
                self.sig_msg.emit(index, 'Under Processing')  # Transmit processing signal
                r = process(fp=fp, shiftInput=shift)
            except:
                # If an exception occurs during execution after try, clear r
                r = []
            if not r:
                # r empty, processing failed
                self.sig_error.emit(index, 'Failed')
                self.sig_result.emit(index, [])
            else:
                if len(r[0]) not in [2, 3, 4]:
                    self.sig_error.emit(index, 'Invalid Data Source')
                    self.fig_result.emit(index, [])
                else:
                    self.sig_result.emit(index, r)
                    self.sig_msg.emit(index, 'successfully')