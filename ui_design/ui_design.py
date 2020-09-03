# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(808, 504)
        self.group_box_files = QtWidgets.QGroupBox(Form)
        self.group_box_files.setGeometry(QtCore.QRect(20, 90, 171, 331))
        self.group_box_files.setObjectName("group_box_files")
        self.gridLayout = QtWidgets.QGridLayout(self.group_box_files)
        self.gridLayout.setObjectName("gridLayout")
        self.table_files = QtWidgets.QTableWidget(self.group_box_files)
        self.table_files.setObjectName("table_files")
        self.table_files.setColumnCount(0)
        self.table_files.setRowCount(0)
        self.gridLayout.addWidget(self.table_files, 0, 0, 1, 1)
        self.group_box_data = QtWidgets.QGroupBox(Form)
        self.group_box_data.setGeometry(QtCore.QRect(210, 90, 291, 341))
        self.group_box_data.setObjectName("group_box_data")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.group_box_data)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.table_results = QtWidgets.QTableWidget(self.group_box_data)
        self.table_results.setObjectName("table_results")
        self.table_results.setColumnCount(0)
        self.table_results.setRowCount(0)
        self.horizontalLayout.addWidget(self.table_results)
        self.group_box_plot = QtWidgets.QGroupBox(Form)
        self.group_box_plot.setGeometry(QtCore.QRect(510, 90, 261, 331))
        self.group_box_plot.setObjectName("group_box_plot")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.group_box_plot)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_plot = QtWidgets.QWidget(self.group_box_plot)
        self.widget_plot.setObjectName("widget_plot")
        self.gridLayout_2.addWidget(self.widget_plot, 0, 0, 1, 1)
        self.widget_header = QtWidgets.QWidget(Form)
        self.widget_header.setGeometry(QtCore.QRect(80, 20, 571, 51))
        self.widget_header.setObjectName("widget_header")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_header)
        self.gridLayout_3.setContentsMargins(20, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_header = QtWidgets.QLabel(self.widget_header)
        self.label_header.setObjectName("label_header")
        self.gridLayout_3.addWidget(self.label_header, 0, 0, 1, 1)
        self.widget_btn = QtWidgets.QWidget(Form)
        self.widget_btn.setGeometry(QtCore.QRect(100, 450, 366, 34))
        self.widget_btn.setObjectName("widget_btn")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_btn)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_btn = QtWidgets.QHBoxLayout()
        self.horizontalLayout_btn.setObjectName("horizontalLayout_btn")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btn.addItem(spacerItem)
        self.btn_import = QtWidgets.QPushButton(self.widget_btn)
        self.btn_import.setObjectName("btn_import")
        self.horizontalLayout_btn.addWidget(self.btn_import)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btn.addItem(spacerItem1)
        self.btn_collate = QtWidgets.QPushButton(self.widget_btn)
        self.btn_collate.setObjectName("btn_collate")
        self.horizontalLayout_btn.addWidget(self.btn_collate)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btn.addItem(spacerItem2)
        self.btn_export = QtWidgets.QPushButton(self.widget_btn)
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout_btn.addWidget(self.btn_export)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_btn.addItem(spacerItem3)
        self.gridLayout_4.addLayout(self.horizontalLayout_btn, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.group_box_files.setTitle(_translate("Form", "Files List"))
        self.group_box_data.setTitle(_translate("Form", "Normalized Data"))
        self.group_box_plot.setTitle(_translate("Form", "Result Graph"))
        self.label_header.setText(_translate("Form", "RSNP System"))
        self.btn_import.setText(_translate("Form", "Import"))
        self.btn_collate.setText(_translate("Form", "Collate"))
        self.btn_export.setText(_translate("Form", "Export"))
