import os

from PyQt5.QtWidgets import QFileDialog
from shutil import copyfile

import globals


def on_save_action(main_widget):
    if globals.SAVE_DESTINATION:
        try:
            copyfile(globals.RESULT_DESTINATION, globals.SAVE_DESTINATION)
        except FileNotFoundError as fnf:
            print(fnf.strerror)
        except:
            print("unknown error")
    else:
        on_save_as_action(main_widget)


def on_save_as_action(main_widget):
    if globals.SAVE_DESTINATION:
        file_location = QFileDialog.getSaveFileName(main_widget, 'Save file',
                                                    globals.SAVE_DESTINATION, "Audio files (*.wav)")
    else:
        file_location = QFileDialog.getSaveFileName(main_widget, 'Save file',
                                                    os.getcwd() + '/resources', "Audio files (*.wav)")
    if file_location[0]:
        try:
            copyfile(globals.RESULT_DESTINATION, file_location[0])
            globals.SAVE_DESTINATION = file_location[0]
        except FileNotFoundError as fnf:
            print(fnf.strerror)
