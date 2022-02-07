import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QWidget, QVBoxLayout, QFileDialog
import matplotlib.pyplot as plt

from matplotlib.backends.backend_template import FigureCanvas

import action_handler
import encryptor_dialog
import speeker_thread
import audio_handler
import audio_line_thread
import globals
import styler
import text_decoder
import preferences_dialog

from main_window import Ui_MainWindow
from plot_widget import Ui_Form
import plot_handler
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        styler.set_style(self, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
        styler.add_style(self, "color", styler.get_text_color(globals.data["APP_COLOR"]))

        styler.set_style(self.ui.menubar, "color", "black")
        styler.add_style(self.ui.menubar, "background-color", "rgb(250, 250, 250)")

        self.ui.scrollArea.verticalScrollBar().setEnabled(False)
        self.ui.scrollArea.setWidgetResizable(True)

        self.test_button = self.ui.pushButton
        self.plotLayout = QHBoxLayout()
        self.wavLayout = QVBoxLayout()
        self.res_plot = None
        self.res_audio_axis = None
        self.test_button.clicked.connect(self._setup_plots)
        self.ui.playButton.clicked.connect(self._start_play)

        self.ui.save_action.triggered.connect(lambda : action_handler.on_save_action(self))
        self.ui.save_as_action.triggered.connect(lambda : action_handler.on_save_as_action(self))
        self.ui.open_action.triggered.connect(lambda : action_handler.on_open_action(self))

        self.dialog = None

        def foo():
            self.dialog = preferences_dialog.preferences(self)
            self.dialog.show()
        self.ui.preferences_action.triggered.connect(foo)
        def bar():
            self.encrypt_dialog = encryptor_dialog.encryptor()
            self.encrypt_dialog.show()
        self.ui.add_relation_action.triggered.connect(bar)

        self.files = None
        # Relation between plot and file: plt => (ind of file in self.files)
        self.plot_file_dict = {}

    # Wav only.
    def fill_plots(self):
        plt.close("all")
        self._clear_layout(self.plotLayout)
        for file_ind in range(len(self.files)):
            wid = self._produce_widget(file_ind)
            styler.set_style(wid, "background-color", "transparent")
            self.plotLayout.addWidget(wid)
        self.update_plot()

    def update_plot(self):
        audio_handler.produce_combined_wav(self.files, globals.data["RESULT_DESTINATION"])
        self.res_plot = plot_handler.get_plot(globals.data["RESULT_DESTINATION"])
        self._clear_layout(self.wavLayout)
        self.wavLayout.addLayout(self.plotLayout)
        self.wavLayout.addWidget(self.res_plot)
        w = QWidget()
        w.setLayout(self.wavLayout)
        self.ui.scrollArea.setWidget(w)

    def update_widgets(self, wid, plot):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            os.getcwd() + '/resources', "Audio files (*.wav)")
        if fname[0]:
            self.files[self.plot_file_dict[wid]] = fname[0]
            plot.close()
            wid.close()
            self.plotLayout.replaceWidget(wid, self._produce_widget(self.plot_file_dict[wid]))
            self.update_plot()

    def _setup_plots(self):
        text = self.ui.plainTextEdit.toPlainText()
        if not text:
            return
        self.files = text_decoder.decode(text)
        self.fill_plots()
        self.ui.save_action.setEnabled(True)
        self.ui.save_as_action.setEnabled(True)


    def _clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            try:
                layout.itemAt(i).widget().setParent(None)
            except:
                layout.itemAt(i).layout().setParent(None)

    def _start_play(self):
        audio_line_thread.scroller(self.ui.scrollArea,
                                   audio_handler.get_plot_data_from_wav(globals.data["RESULT_DESTINATION"])).start()

        speeker_thread.speeker(globals.data["RESULT_DESTINATION"]).start()

    def _produce_widget(self, file_ind):
        plt_widget = QWidget()
        Ui_Form().setupUi(plt_widget, self.files[file_ind], plot_handler.get_plot(self.files[file_ind]), self)
        self.plot_file_dict[plt_widget] = file_ind
        return plt_widget


globals.update_params()
app = QtWidgets.QApplication([])
application = mywindow()

application.show()
sys.exit(app.exec())
