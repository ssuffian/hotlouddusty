from datetime import datetime
from multiprocessing import Process
import os
import psutil
import time

def write_to_file(filepath, val1, val2, cols = ["db", "rms"], now_str=None):
    if now_str is None:
        now_str = datetime.now().isoformat()

    if os.path.isfile(filepath):
        with open(filepath, 'a') as f:
            f.write("{},{},{}\n".format(now_str, val1, val2))
    else:
        with open(filepath, 'a') as f:
            f.write("datetime,{}\n".format(",".join(cols)))
            f.write("{},{},{}\n".format(now_str, val1, val2))

class myThread(Process):
    def __init__(self, function):
        Process.__init__(self)
        self.function = function

    def run(self):
        while True:
            self.function()

def run_thread_loop(function, loop_secs=5, kill_wait_secs=5):
    while True:
        p = myThread(function)
        p.start()
        p.join(loop_secs)
        if p.is_alive():
            p.terminate()
            for pid in psutil.pids():
                if p.pid == pid:
                    os.system("kill "+str(pid))
                    time.sleep(kill_wait_secs)
