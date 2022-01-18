import math
import time
from threading import Thread


class scroller(Thread):
    def __init__(self, sa, dt, slides=75):
        super(scroller, self).__init__()
        self.daemon = True
        self.vb = sa.horizontalScrollBar()
        self.dt = dt
        self.slides = slides

    def run(self):
        _, frame_count, length = self.dt
        for x in range(0, int(frame_count) + 1, int(frame_count/self.slides)):
            self.vb.setValue(int(self.vb.maximum() * x / frame_count))
            time.sleep(length / self.slides)