import json
import os


splitters = [".", ",", " ", ";", ":", ""]


def _check_separator(ind, word_len, text):
    if word_len == 1:
        return True
    elif ind + word_len == len(text):
        return True
    elif ind == 0:
        return text[ind + word_len] in splitters
    else:
        return text[ind - 1] in splitters and text[ind + word_len] in splitters


def decode(text):
    with open(os.getcwd() + r"/data.json", "r") as read_file:
        data = json.load(read_file)
    filenames = []
    file_dict = {}
    text = text.lower()

    # TODO morph into queue

    for key in sorted(data.keys(), key=len, reverse=True):
        ind = 0
        while ~(ind := text.find(key, ind)):
            if _check_separator(ind, len(key), text):
                file_dict[ind] = key
                text = text.replace(key, " "*len(key), 1)
            ind += 1

    for i in sorted(file_dict):
        filenames.append(data[file_dict[i]])

    return [file_name for file_name in filenames]
