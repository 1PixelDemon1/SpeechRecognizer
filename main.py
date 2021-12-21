from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QVBoxLayout

from matplotlib.backends.backend_template import FigureCanvas

import speeker_thread
import audio_handler
import audio_line_thread
import globals
import text_decoder
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

        self.test_button = self.ui.pushButton
        self.plotLayout = QHBoxLayout()
        self.wavLayout = QVBoxLayout()
        self.res_plot = None
        self.res_audio_axis = None
        self.test_button.clicked.connect(self._start_play)

    # Wav only.
    def fill_plots(self, files):
        self._clear_layout(self.plotLayout)
        for file in files:
            self.plotLayout.addWidget(plot_handler.get_plot(file))
        self.update_plot(files)

    def update_plot(self, files):
        audio_handler.produce_combined_wav(files, globals.RESULT_DESTINATION)
        self.res_plot = plot_handler.get_plot(globals.RESULT_DESTINATION)
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

    def _start_play(self):
        self.fill_plots(text_decoder.decode(self.ui.plainTextEdit.toPlainText()))

        audio_line_thread.scroller(self.ui.scrollArea,
                                   audio_handler.get_plot_data_from_wav(globals.RESULT_DESTINATION)).start()

        speeker_thread.speeker(globals.RESULT_DESTINATION).start()


app = QtWidgets.QApplication([])
application = mywindow()
# application.fill_plots([f"resources/gen-{i}.wav" for i in range(6, 12)])

application.show()
sys.exit(app.exec())
