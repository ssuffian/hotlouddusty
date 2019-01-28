import audioop
import psutil
import pyaudio
import os
import math

from helpers import write_to_file, run_thread_loop

LOUD_FILEPATH = '../data/loud.csv'

class Loud():

    def __init__(self):
        self.chunk = 10000

    def record(self):
        p = pyaudio.PyAudio()
        stream = p.open(format = pyaudio.paInt16,
            channels = 2,
            rate = 44100,
            input = True,
            frames_per_buffer = self.chunk
        )
        data = stream.read(self.chunk)
        rms_val = audioop.rms(data, 2)
        dbs_val = (max(20.0*math.log(rms_val, 10), -60.0))
        print(dbs_val)
        write_to_file(
            LOUD_FILEPATH,
            round(dbs_val, 2),
            round(rms_val, 2),
            ["db", "rms"],
        )
        stream.close()
        p.terminate()


if __name__ == '__main__':
    run_thread_loop(Loud().record, loop_secs=15)
