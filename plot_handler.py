import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import globals
import audio_handler


def get_plot(file):
    figure = plt.figure()
    canvas = FigureCanvas(figure)
    ax = figure.add_subplot()
    ax.plot(audio_handler.get_data_from_wav(file)[1],
            color='#' + ''.join(f'{i:02X}' for i in globals.data["PLOT_LINE_COLOR"]))
    ax.axis("off")
    figure.set_facecolor(globals.data["PLOT_FACE_COLOR"])
    canvas.setMinimumWidth(round(canvas.frameGeometry().width() / 2))
    return canvas

