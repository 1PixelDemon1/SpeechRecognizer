import json
import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog

import globals
import styler
from encryptor_window import Ui_Dialog
from pathlib import Path

class encryptor(QtWidgets.QDialog):
    def __init__(self):
        super(encryptor, self).__init__()

        self.cur_row = 0
        self.can_save = True

        styler.set_style(self, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
        styler.add_style(self, "color", styler.get_text_color(globals.data["APP_COLOR"]))

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        styler.set_style(self.ui.tableWidget.horizontalHeader(), "color", "black")
        styler.set_style(self.ui.tableWidget.verticalHeader(), "color", "black")

        self.ui.confirm_button.clicked.connect(self.on_save)
        self.ui.path_button.clicked.connect(self.path_file)
        self.ui.del_button.clicked.connect(self.rm_row)
        self.ui.add_button.clicked.connect(self.add_row)

        self.fill()

    def fill(self):
        with open(os.getcwd() + r"/data.json", "r") as read_file:
            data = json.load(read_file)
        self.ui.tableWidget.setRowCount(len(data))
        for item in enumerate(data.items()):
            self.ui.tableWidget.setItem(item[0], 0, QtWidgets.QTableWidgetItem(item[1][0]))
            self.ui.tableWidget.setItem(item[0], 1, QtWidgets.QTableWidgetItem(item[1][1]))

    def rm_row(self):
        self.cur_row = self.ui.tableWidget.currentRow()
        if self.cur_row is not None:
            self.ui.tableWidget.removeRow(self.cur_row)

    def add_row(self):
        self.cur_row = self.ui.tableWidget.currentRow()

        if not self.ui.tableWidget.rowCount():
            self.cur_row = 0

        if self.cur_row is not None:
            self.ui.tableWidget.insertRow(self.cur_row)
            self.ui.tableWidget.setItem(self.cur_row, 0, QtWidgets.QTableWidgetItem(""))
            self.ui.tableWidget.setItem(self.cur_row, 1, QtWidgets.QTableWidgetItem(""))

    def path_file(self):
        self.cur_row = self.ui.tableWidget.currentRow()

        if self.cur_row is not None:
            filename, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                      os.getcwd() + '/resources', "Audio files (*.wav)")
            if filename:
                self.ui.tableWidget.setItem(self.cur_row, 1, QtWidgets.QTableWidgetItem(filename))

    def on_save(self):
        self.can_save = True
        for row in range(self.ui.tableWidget.rowCount()):

            if not self.ui.tableWidget.item(row, 0).text():
                self.ui.tableWidget.item(row, 0).setBackground(QColor(255, 0, 0))
                self.can_save = False
            else:
                self.ui.tableWidget.item(row, 0).setBackground(QColor(0, 0, 0, 0))

            if not Path(self.ui.tableWidget.item(row, 1).text()).is_file() and\
               not Path(f"{os.getcwd()}/{self.ui.tableWidget.item(row, 1).text()}").is_file():

                self.ui.tableWidget.item(row, 1).setBackground(QColor(255, 0, 0))
                self.can_save = False
            else:
                self.ui.tableWidget.item(row, 1).setBackground(QColor(0, 0, 0, 0))

        if self.can_save:
            self.commit_save()

    def commit_save(self):
        data_to_save = dict()
        for row in range(self.ui.tableWidget.rowCount()):
            data_to_save[self.ui.tableWidget.item(row, 0).text()] = self.ui.tableWidget.item(row, 1).text()
        with open(os.getcwd() + r"/data.json", "w") as write_file:
            json.dump(data_to_save, write_file, indent=4)
