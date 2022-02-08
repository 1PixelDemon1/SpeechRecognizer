import os

from PyQt5.QtWidgets import QFileDialog
from shutil import copyfile
from striprtf.striprtf import rtf_to_text

import globals


def on_open_action(main_widget):
    fname = QFileDialog.getOpenFileName(main_widget, 'Open file',
                                        os.getcwd() + r"/text sources", "Text files (*.txt *.rtf)")
    if fname[0]:
        with open(fname[0], "r", encoding="UTF8") as text_file:
            rtf = "some rtf encoded string"
            text = text_file.read()
            # rtf needs some extra converting.
            if fname[0][-3:] == "rtf":
                text = rtf_to_text(text, errors="ignore")
            main_widget.ui.plainTextEdit.setPlainText(text)


def on_save_action(main_widget):
    if globals.data["SAVE_DESTINATION"]:
        try:
            copyfile(globals.data["RESULT_DESTINATION"], globals.data["SAVE_DESTINATION"])
        except FileNotFoundError as fnf:
            print(fnf.strerror)
        except:
            print("unknown error")
    else:
        on_save_as_action(main_widget)


def on_save_as_action(main_widget):
    if globals.data["SAVE_DESTINATION"]:
        file_location = QFileDialog.getSaveFileName(main_widget, 'Save file',
                                                    globals.data["SAVE_DESTINATION"], "Audio files (*.wav)")
    else:
        file_location = QFileDialog.getSaveFileName(main_widget, 'Save file',
                                                    os.getcwd() + '/resources', "Audio files (*.wav)")
    if file_location[0]:
        try:
            copyfile(globals.data["RESULT_DESTINATION"], file_location[0])
            globals.data["SAVE_DESTINATION"] = file_location[0]
            # TODO for future.
            # globals.update_file()
        except FileNotFoundError as fnf:
            print(fnf.strerror)
