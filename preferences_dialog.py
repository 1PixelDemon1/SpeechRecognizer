from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QColorDialog
import globals
import styler
from preferences_window import Ui_Dialog


class preferences(QtWidgets.QDialog):
    def __init__(self, main_widget):
        super(preferences, self).__init__()
        styler.set_style(self, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
        styler.add_style(self, "color", styler.get_text_color(globals.data["APP_COLOR"]))

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        border_color = styler.get_text_color(globals.data["APP_COLOR"])
        styler.set_style(self.ui.app_color, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
        styler.add_style(self.ui.app_color, "border", "1px solid " + border_color)
        styler.set_style(self.ui.audio_wave, "background-color", styler.get_string_from_rgb(
            list(map(lambda x: x*255, globals.data["PLOT_FACE_COLOR"]))))
        styler.add_style(self.ui.audio_wave, "border", "1px solid " + border_color)
        styler.set_style(self.ui.wave_color, "background-color",
                         styler.get_string_from_rgb(globals.data["PLOT_LINE_COLOR"]))
        styler.add_style(self.ui.wave_color, "border", "1px solid " + border_color)

        self.color_buffer = None

        def change_app(event):
            self.changeColor(QColor(globals.data["APP_COLOR"][0], globals.data["APP_COLOR"][1], globals.data["APP_COLOR"][2]))
            if self.color_buffer is not None:
                globals.data["APP_COLOR"] = [self.color_buffer.red(), self.color_buffer.green(), self.color_buffer.blue()]

                styler.set_style(self, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
                styler.add_style(self, "color", styler.get_text_color(globals.data["APP_COLOR"]))

                styler.add_style(self.ui.app_color, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))

                styler.set_style(main_widget, "background-color", styler.get_string_from_rgb(globals.data["APP_COLOR"]))
                styler.add_style(main_widget, "color", styler.get_text_color(globals.data["APP_COLOR"]))

        def change_plot_face(event):
            self.changeColor(QColor(int(globals.data["PLOT_FACE_COLOR"][0] * 255), int(globals.data["PLOT_FACE_COLOR"][1] * 255),
                                    int(globals.data["PLOT_FACE_COLOR"][2] * 255)))
            if self.color_buffer is not None:
                globals.data["PLOT_FACE_COLOR"] = (self.color_buffer.red()/255,
                                                   self.color_buffer.green()/255, self.color_buffer.blue()/255)
                styler.add_style(self.ui.audio_wave, "background-color", styler.get_string_from_rgb(
                    list(map(lambda x: x * 255, globals.data["PLOT_FACE_COLOR"]))))
                if main_widget.files is not None:
                    main_widget.fill_plots()

        def change_plot_color(event):
            self.changeColor(QColor(globals.data["PLOT_LINE_COLOR"][0], globals.data["PLOT_LINE_COLOR"][1],
                                    globals.data["PLOT_LINE_COLOR"][2]))
            if self.color_buffer is not None:
                globals.data["PLOT_LINE_COLOR"] = (self.color_buffer.red(),
                                                   self.color_buffer.green(),
                                                   self.color_buffer.blue())
                styler.add_style(self.ui.wave_color, "background-color",
                                 styler.get_string_from_rgb(globals.data["PLOT_LINE_COLOR"]))
                if main_widget.files is not None:
                    main_widget.fill_plots()

        self.ui.app_color.mouseReleaseEvent = change_app
        self.ui.audio_wave.mouseReleaseEvent = change_plot_face
        self.ui.wave_color.mouseReleaseEvent = change_plot_color

        self.ui.cancelButton.clicked.connect(self.close)

        def save_close():
            globals.update_file()
            self.close()

        self.ui.ok_button.clicked.connect(save_close)

    def changeColor(self, color=QColor(128, 128, 128)):
        self.color_buffer = QColorDialog.getColor(color, self, "Выберите цвет")
        if not self.color_buffer.isValid():
            self.color_buffer = None
