import pydub
import wave
from scipy.io import wavfile


def get_data_from_wav(file):
    return wavfile.read(file)


def produce_combined_wav(files, path):
    res = pydub.AudioSegment.empty()
    for file in files:
        res += pydub.AudioSegment.from_wav(file)

    with wave.open(path, "wb") as out_f:
        out_f.setnchannels(res.channels)
        out_f.setsampwidth(res.sample_width)
        out_f.setframerate(res.frame_rate)
        out_f.writeframesraw(res.raw_data)
