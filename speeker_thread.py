from threading import Thread
import simpleaudio as sa


class speeker(Thread):
    def __init__(self, file_name):
        super(speeker, self).__init__()
        self.setDaemon(True)
        self.file_name = file_name

    def run(self):
        wave_obj = sa.WaveObject.from_wave_file(self.file_name)
        play_obj = wave_obj.play()
        play_obj.wait_done()
