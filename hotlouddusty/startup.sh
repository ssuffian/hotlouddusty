#!/bin/sh
adb forward tcp:20175 tcp:50000
pkill screen
screen -dmS hot bash -c 'cd ~/hotlouddusty/hotlouddusty; python hot.py'
screen -dmS loud bash -c 'cd ~/hotlouddusty/hotlouddusty; python loud.py'
screen -dmS dusty bash -c 'cd ~/hotlouddusty/hotlouddusty; python dusty.py'
screen -dmS where bash -c 'cd ~/hotlouddusty/hotlouddusty; python where.py'
