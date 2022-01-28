from PyQt5.QtGui import QColor


def set_style(obj, param, value):
    obj.setStyleSheet(f"{param}:{value};")


def add_style(obj, param, value):
    obj.setStyleSheet(obj.styleSheet() + f"{param}:{value};")


def get_text_color(rgb_value: QColor):
    return "black" if rgb_value.red() + rgb_value.green() + rgb_value.blue() > 128 * 2 else "white"


def get_text_color(rgb_value: list):
    return "black" if sum(rgb_value) > 128 * 2 else "white"


def get_string_from_rgb(rgb_value: QColor):
    return f"rgb({rgb_value.red()}, {rgb_value.green()}, {rgb_value.blue()})"


def get_string_from_rgb(rgb_value: list):
    return "rgb(" + ",".join(map(lambda x: str(x), rgb_value)) + ")"
