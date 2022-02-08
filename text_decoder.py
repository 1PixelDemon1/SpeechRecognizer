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
    text = text.lower()

    flag = True
    while flag:
        flag = False
        for key in sorted(data.keys(), key=len, reverse=True):
            ind = text.find(key)

            if ind == -1:
                continue

            if (ind == 0 or all(i in splitters for i in text[0:ind])) and\
                    _check_separator(ind, len(key), text):

                filenames.append(data[key])
                text = text.replace(key, "", 1)
                flag = True
                break

    return filenames
