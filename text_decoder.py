_temp = {
    "а": "gen-6.wav",
    "б": "gen-7.wav",
    "в": "gen-8.wav",
    "г": "gen-9.wav",
    "д": "gen-10.wav",
    "е": "gen-11.wav",
    "ж": "gen-13.wav",
    "з": "gen-14.wav",
    "и": "gen-15.wav",
    "й": "gen-16.wav",
    "к": "gen-17.wav",
    "л": "gen-18.wav",
    "м": "gen-19.wav",
    "н": "gen-20.wav",
    "о": "gen-21.wav",
    "п": "gen-22.wav",
    "р": "gen-23.wav",
    "с": "gen-24.wav",
    "т": "gen-25.wav",
    "у": "gen-26.wav",
    "ф": "gen-27.wav",
    "х": "gen-28.wav",
    "ц": "gen-29.wav",
    "ч": "gen-30.wav",
    "ш": "gen-31.wav",
    "щ": "gen-32.wav",
    "ъ": "gen-33.wav",
    "ы": "gen-34.wav",
    "ь": "gen-35.wav",
    "э": "gen-36.wav",
    "ю": "gen-37.wav",
    "я": "gen-38.wav",
    "ё": "gen-40.wav",
    "на": "gen-37.wav",
    "дороге": "gen-38.wav",
    "на дороге": "on_road.wav",

}

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
    filenames = []
    file_dict = {}
    text = text.lower()

    for key in sorted(_temp.keys(), key=len, reverse=True):
        ind = 0
        while ~(ind := text.find(key, ind)):
            if _check_separator(ind, len(key), text):
                file_dict[ind] = key
                text = text.replace(key, " "*len(key), 1)
            ind += 1

    for i in sorted(file_dict):
        filenames.append(_temp[file_dict[i]])

    return [r"resources/" + file_name for file_name in filenames]
