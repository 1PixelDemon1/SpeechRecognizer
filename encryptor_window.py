# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EncryptorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(664, 486)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confirm_button = QtWidgets.QPushButton(Dialog)
        self.confirm_button.setObjectName("confirm_button")
        self.horizontalLayout.addWidget(self.confirm_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.path_button = QtWidgets.QPushButton(Dialog)
        self.path_button.setEnabled(True)
        self.path_button.setFlat(False)
        self.path_button.setObjectName("path_button")
        self.horizontalLayout.addWidget(self.path_button)
        self.add_button = QtWidgets.QPushButton(Dialog)
        self.add_button.setEnabled(True)
        self.add_button.setDefault(False)
        self.add_button.setFlat(False)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.del_button = QtWidgets.QPushButton(Dialog)
        self.del_button.setEnabled(True)
        self.del_button.setObjectName("del_button")
        self.horizontalLayout.addWidget(self.del_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Зависимости"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Ключ-фраза"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Файл"))
        self.confirm_button.setText(_translate("Dialog", "Сохранить"))
        self.path_button.setText(_translate("Dialog", "Путь"))
        self.add_button.setText(_translate("Dialog", "+"))
        self.del_button.setText(_translate("Dialog", "-"))
