#!/bin/sh
pkill screen
screen -dmS display bash -c 'cd ~/hotlouddusty/hotlouddusty; python3 display/display.py'
