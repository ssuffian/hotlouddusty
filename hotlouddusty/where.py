import pynmea2
import time
import socket

from helpers import write_to_file

WHERE_FILEPATH = "../data/where.csv"
WHERE_PORT = 20175

class Where():
    def __init__(self, port=WHERE_PORT, localhost='0.0.0.0'):
        print("Init Where")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((localhost, WHERE_PORT))

    def record(self):
        try:
            while True:
                time.sleep(1)
                lines = (self.sock.recv(1024).decode('utf-8').split('\n'))
                for line in lines:
                    if line.startswith('$GPGGA'):
                        msg = pynmea2.parse(line)
                        print(msg.latitude, msg.longitude)
                        write_to_file(
                            WHERE_FILEPATH,
                            msg.latitude,
                            msg.longitude,
                            cols=["latitude", "longitude"],
                        )
        except:
            raise
        finally:
            self.sock.close()

if __name__ == '__main__':
    Where().record()
