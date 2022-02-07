import os

from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog, QFileDialog

import globals
import styler
import text_decoder
from encryptor_window import Ui_Dialog


class encryptor(QtWidgets.QDialog):
    def __init__(self):
        super(encryptor, self).__init__()

        self.cur_row = 0
        styler.set_style(self, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
        styler.add_style(self, "color", styler.get_text_color(globals.data["APP_COLOR"]))

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        styler.set_style(self.ui.tableWidget.horizontalHeader(), "color", "black")
        styler.set_style(self.ui.tableWidget.verticalHeader(), "color", "black")
        self.ui.path_button.clicked.connect(self.path_file)
        self.ui.del_button.clicked.connect(self.rm_row)
        self.ui.add_button.clicked.connect(self.add_row)

        self.ui.tableWidget.doubleClicked.connect(self.on_clicked)
        self.ui.tableWidget.clicked.connect(self.on_activated)

        # TODO add json
        self.fill()

    def fill(self):
        self.ui.tableWidget.setRowCount(len(text_decoder._temp))
        for item in enumerate(text_decoder._temp.items()):
            self.ui.tableWidget.setItem(item[0], 0, QtWidgets.QTableWidgetItem(item[1][0]))
            self.ui.tableWidget.setItem(item[0], 1, QtWidgets.QTableWidgetItem(item[1][1]))

    def rm_row(self):
        if self.cur_row is not None:
            self.ui.tableWidget.removeRow(self.cur_row)

    def add_row(self):
        if self.cur_row is not None:
            self.ui.tableWidget.insertRow(self.cur_row)

    def path_file(self):
        if self.cur_row is not None:
            filename, _ = QFileDialog.getOpenFileName(self, 'Open file',
                                                      os.getcwd() + '/resources', "Audio files (*.wav)")
            if filename:
                self.ui.tableWidget.setItem(self.cur_row, 1, QtWidgets.QTableWidgetItem(filename))
            self.ui.path_button.setEnabled(False)

    def on_activated(self, item):
        self.cur_row = item.row()
        self.ui.del_button.setEnabled(True)
        self.ui.add_button.setEnabled(True)

    def on_clicked(self, item):
        # We only want to give access to path for second col.
        if item.column() == 1:
            self.cur_row = item.row()
            self.ui.path_button.setEnabled(True)
