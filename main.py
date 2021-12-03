from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import audio_handler
import globals
from main_window import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.scrollArea.verticalScrollBar().setEnabled(False)
        self.ui.scrollArea.setWidgetResizable(True)

        self.plotLayout = QHBoxLayout()
        self.wavLayout = QVBoxLayout()

        self.fill_plots()

    def fill_plots(self):
        for i in range(8, 12):
            self.plotLayout.addWidget(self._get_plot(f"resources/gen-{i}.wav"))

        figure = plt.figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        ax.plot(audio_handler.produce_combined_wav([f"resources/gen-{i}.wav" for i in range(8, 12)], "resources/result.wav"))
        ax.axis("off")
        figure.set_facecolor(globals.PLOT_FACE_COLOR)
        canvas.setMinimumWidth(round(canvas.frameGeometry().width() / 2))

        self.wavLayout.addLayout(self.plotLayout)
        self.wavLayout.addWidget(canvas)
        w = QWidget()
        w.setLayout(self.wavLayout)
        self.ui.scrollArea.setWidget(w)

    def _get_plot(self, file):
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()
        ax.plot(audio_handler.get_data_from_wav(file)[1])
        ax.axis("off")
        figure.set_facecolor(globals.PLOT_FACE_COLOR)
        canvas.setMinimumWidth(round(canvas.frameGeometry().width() / 2))
        return canvas


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
