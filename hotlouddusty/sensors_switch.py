import sys

sensor_status_filepath = '../data/sensors_status.txt'

def get_sensor_status():
    with open(sensor_status_filepath, 'r') as f:
        return f.read()

def change_sensor_status(command):
    if command.lower() == "on":
        status = "1"
    elif command.lower() == "off":
        status = "0"
    with open(sensor_status_filepath, 'w') as f:
        f.write(status)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must include a command 'on' or 'off'")
    else:
        change_sensor_status(sys.argv[1])
        print("Changed sensor status to {}".format(get_sensor_status()))
