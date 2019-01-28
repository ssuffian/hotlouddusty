from datetime import datetime
import os
import time

from sds011 import SDS011
import sensors_switch

from helpers import write_to_file

DUSTY_SENSOR_FREQUENCY_SECONDS = 1
DUSTY_SENSOR_BOOT_DELAY_SECONDS = 5
DUSTY_FILEPATH = '../data/dusty.csv'
DUSTY_DEV_USB = '/dev/ttyUSB0'

class Dusty():
    def __init__(self):
        self.sensor = SDS011(DUSTY_DEV_USB, use_query_mode=True)

    def start(self):
        self.sensor.sleep(sleep=False)
        time.sleep(DUSTY_SENSOR_BOOT_DELAY_SECONDS)

    def record(self):
        time.sleep(DUSTY_SENSOR_FREQUENCY_SECONDS)
        value = self.sensor.query()
        write_to_file(
            DUSTY_FILEPATH,
            value[0],
            value[1],
            ["pm2.5", "pm10"],
        )
        print(value[0], value[1])

    def stop(self):
       self.sensor.sleep()

    def run_pm(self):
        self.start()
        try:
            while True:
                self.record()
        except:
            raise
        finally:
            self.stop()

if __name__ == "__main__":
    Dusty().run_pm()
