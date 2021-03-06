# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, fileName, plot, main_widget):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileName = QtWidgets.QLabel(Form)
        self.fileName.setObjectName("fileName")
        self.horizontalLayout.addWidget(self.fileName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.changeFileButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeFileButton.sizePolicy().hasHeightForWidth())
        self.changeFileButton.setSizePolicy(sizePolicy)
        self.changeFileButton.setObjectName("changeFileButton")

        self.horizontalLayout.addWidget(self.changeFileButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.plotContainerWidget = QtWidgets.QWidget(Form)
        self.plotContainerWidget.setObjectName("plotContainerWidget")
        self.plotContainerWidget = plot
        self.verticalLayout.addWidget(self.plotContainerWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.changeFileButton.clicked.connect(lambda : main_widget.update_widgets(self.verticalLayout.parentWidget(), plot))

        self.retranslateUi(Form, fileName)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form, fileName):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fileName.setText(_translate("Form", fileName))
        self.changeFileButton.setText(_translate("Form", "???"))

