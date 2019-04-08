import Adafruit_DHT

from helpers import write_to_file, run_thread_loop

PIN = 23
HOT_FILEPATH = '../data/hot.csv'

class Hot():

    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = PIN

    def record(self):
        humidity, temperature = Adafruit_DHT.read_retry(
            self.sensor, self.pin
        )
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            write_to_file(
                HOT_FILEPATH,
                round(temperature, 2),
                round(humidity, 2),
                ["temperature_c", "humidity"],
            )
        else:
            print('Failed to get reading. Try again!')


if __name__ == '__main__':
    run_thread_loop(Hot().record, loop_secs=600000)
