#!/bin/sh
adb forward tcp:20175 tcp:50000
pkill screen
screen -dmS hot bash -c 'cd ~/hotlouddusty/hotlouddusty; python3 hot.py'
screen -dmS loud bash -c 'cd ~/hotlouddusty/hotlouddusty; python3 loud.py'
screen -dmS dusty bash -c 'cd ~/hotlouddusty/hotlouddusty; python3 dusty.py'
screen -dmS where bash -c 'cd ~/hotlouddusty/hotlouddusty; python3 where.py'
