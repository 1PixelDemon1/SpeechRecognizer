import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import globals
import audio_handler


def get_plot(file):
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    ax = figure.add_subplot()
    ax.plot(audio_handler.get_data_from_wav(file)[1])
    ax.axis("off")
    figure.set_facecolor(globals.PLOT_FACE_COLOR)
    canvas.setMinimumWidth(round(canvas.frameGeometry().width() / 2))
    return canvas


def draw_audio_line_at(ax, time_stamp, clear=True):
    if clear:
        ax.clear()
    ax.axis("off")
    ax.axvline(x=time_stamp)
