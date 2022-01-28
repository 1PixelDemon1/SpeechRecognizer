import os
import json


data = None


def update_params():
    with open(os.getcwd() + r"/preferences.json", "r") as read_file:
        global data
        data = json.load(read_file)


def update_file():
    with open(os.getcwd() + r"/preferences.json", "w") as write_file:
        json.dump(data, write_file, indent=4)


