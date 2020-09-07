# coding: utf-8

from PyQt5 import QtGui, QtCore, QtWidgets
from ui_design.ui_design import Ui_Form
import os


class WidgetMain(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setupUi(self)  # Initialize Ui
        self.setWindowTitle('RSNP System')  # window title
        # use QSplitter Drag to adjust the three main box
        self.horizontal_splitter = QtWidgets.QSplitter(orientation=QtCore.Qt.Horizontal, parent=self)
        # Add three boxes separately
        self.horizontal_splitter.addWidget(self.group_box_files)
        self.horizontal_splitter.addWidget(self.group_box_data)
        self.horizontal_splitter.addWidget(self.group_box_plot)
        # files and data constant,  plot changes according to stretching
        self.horizontal_splitter.setStretchFactor(2, QtWidgets.QHeaderView.Stretch)
        # setup a vertical layout
        layout = QtWidgets.QVBoxLayout(self)
        # Layout margins No margins
        layout.setContentsMargins(0, 0, 0, 0)
        # Add header ,horizontal splitter and button to layout
        layout.addWidget(self.widget_header)
        layout.addWidget(self.horizontal_splitter, )
        layout.addWidget(self.widget_btn)
        # Keep splitter part stretched
        layout.setStretchFactor(self.horizontal_splitter, QtWidgets.QHeaderView.Stretch)
        self.setLayout(layout)  # Update the layout
        # Set style
        self.setStyleSheet('''
        #widget_header{
          min-height: 60px; 
          background-color: #4F4B4B;  
        }
        #label_header{
          color: white;
          font: 16pt "Arial";
        }
        
        ''')

        self.init_table_results()  # call table results
        self.init_table_files()    # call file list
        # A click event that binds the import
        self.btn_import.clicked.connect(self.handle_select_and_import_files)
        # Create a new variable storage file path and data
        self.data_files = []
        # Bind the function to edit the cell of the file list
        self.table_files.itemChanged.connect(self.handle_user_edit_param)

        # start process
        self.process_service = ProcessService(self)

    def init_table_files(self):
        """Initialization file list table"""
        self.table_files.clear()  # clear the list
        self.table_files.setRowCount(0)  # Initial 0 lines
        self.table_files.setColumnCount(3)  # Three columns show file status
        #  Set the text displayed in the horizontal header in order
        self.table_files.setHorizontalHeaderLabels(['File', 'Param', 'Status'])

    def init_table_results(self):
        """Initialization result table"""
        self.table_results.clear()  # clear the list
        self.table_results.setRowCount(0)  # Initial 0 lines
        self.table_results.setColumnCount(2)  # Two columns show file results
        #  Set the text displayed in the horizontal header in order
        self.table_results.setHorizontalHeaderLabels(['X', 'N'])

    def handle_select_and_import_files(self):
        """Process user selection and import txt files"""
        # Open file and get file list(ls)
        ls, _ext = QtWidgets.QFileDialog.getOpenFileNames(
            parent=self, caption='Import Data Files', directory='.', filter='Txt Data Files(*.txt)'
            )
        #  Open the txt file in the current path
        #  Determine whether to choose
        if not ls:
            return
        ls.sort()  # Sort file list
        #  Block external signals
        self.table_files.blockSignals(True)
        #  List of files
        for c, fp in enumerate(ls):
            #  Get the current number of rows
            r = self.table_files.rowCount()
            #  Insert the row in the table
            self.table_files.insertRow(r)
            #  Insert list by line number [path, Param, results]
            self.data_files.insert(r, [fp, None, None])
            #  creat cell with txt name
            item = QtWidgets.QTableWidgetItem()
            item.setText(os.path.split(fp)[1])  # slice the path to get the file name and set
            item.setStatusTip(fp)  # mouse over to display the file path
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled)  # is enabled
            #  Set the item in the specified row and first column as a QTableWidgetItem instance object
            self.table_files.setItem(r, 0, item)
            # Set the editable content of the cell as the offset
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)  # center aligned offsets
            item.setStatusTip(fp)
            #  can only edit, nothing else
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
            #  Set the second column
            self.table_files.setItem(r, 1, item)
            #  Create a cell to display the state of the text
            item = QtWidgets.QTableWidgetItem()
            #  Set the newly imported file to the new import state
            item.setText('New Imported')
            item.setTextAlignment(QtCore.Qt.AlignCenter)  # center aligned
            item.setStatusTip(fp)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled)
            #  #  Set the third column
            self.table_files.setItem(r, 2, item)
        # Turn off signal blocking
        self.table_files.blockSignals(False)

    def handle_user_edit_param(self, item: QtWidgets.QTableWidgetItem):
        """Process user edit offset"""
        r = item.row()  # get Row number of the cell
        c = item.column()  # get Column number of the cell
        #  If it is not the parameter in the second column, it cannot be edited
        if c != 1:
            return
        #  Get the contents of the cell into data
        data = item.text()
        #  Block signal
        self.table_files.blockSignals(True)
        #  Determine whether the data type of data is correct
        try:
            data = float(data)
            # Display white correctly
            item.setBackground(QtGui.QBrush(QtCore.Qt.white))
        #  The wrong data type cannot be converted, the yellow prompt is displayed
        except ValueError:
            item.setText('')
            item.setBackground(QtGui.QBrush(QtCore.Qt.yellow))
            #  Reset data
            data = None
        #  Pass the data value to the param place in the datalist
        self.data_files[r][1] = data
        print(self.data_files)
        #  Unblock signal
        self.table_files.blockSignals(False)

    def handle_receive_result(self, index: int, result: list):
        """Inspection data collation results"""
        #  If the result exists, mark a new status
        if result:
            self.table_files.blockSignals(True)
            self.table_files.item(index, 2).setText("")
            self.table_files.blockSignals(False)
        self.data_files[index][2] = result
        #  If the result does not exist, the unlock button is operated again
        if index == len(self.data_files) - 1:
            self.btn_import.setDisabled(False)
            self.btn_collate.setDisabled(False)
            self.btn_export.setDisabled(False)

    def handle_start_process(self):
        """Click the button to start processing"""

        self.btn_import.setDisabled(True)
        self.btn_collate.setDisabled(True)
        self.btn_export.setDisabled(True)

        self.procee_service.start()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = WidgetMain()
    w.show()
    sys.exit(app.exec_())
