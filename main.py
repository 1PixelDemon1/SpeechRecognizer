from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

import audio_handler
import globals
from main_window import Ui_MainWindow
import plot_handler
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
        self.res_plot = None
        self.res_audio_axis = None

    # Wav only.
    def fill_plots(self, files):
        self._clear_layout(self.plotLayout)
        for file in files:
            self.plotLayout.addWidget(plot_handler.get_plot(file))
        self.update_plot(files)

    def update_plot(self, files):
        audio_handler.produce_combined_wav(files, globals.RESULT_DESTINATION)
        self.res_plot = plot_handler.get_plot(globals.RESULT_DESTINATION)
        self.res_audio_axis = self.res_plot.figure.get_axes()[0].twinx()
        self.res_audio_axis.axis("off")
        self._clear_layout(self.wavLayout)
        self.wavLayout.addLayout(self.plotLayout)
        self.wavLayout.addWidget(self.res_plot)
        w = QWidget()
        w.setLayout(self.wavLayout)
        self.ui.scrollArea.setWidget(w)

    def _clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            try:
                layout.itemAt(i).widget().setParent(None)
            except:
                layout.itemAt(i).layout().setParent(None)


app = QtWidgets.QApplication([])
application = mywindow()
application.fill_plots([f"resources/gen-{i}.wav" for i in range(6, 12)])
plot_handler.draw_audio_line_at(application.res_audio_axis, 4000)
application.show()
sys.exit(app.exec())