import pydub
import numpy as np
from scipy.io import wavfile


def get_data_from_wav(file):
    return wavfile.read(file)


def produce_combined_wav(files, path):
    res = pydub.AudioSegment.empty()
    for file in files:
        res += pydub.AudioSegment.from_wav(file)
    res.export(path, format="wav")
    return np.frombuffer(res.raw_data, dtype=np.int)
