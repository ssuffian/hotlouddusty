#!/bin/sh
if ! screen -list | grep -q "display"; then
        screen -dmS display bash -c 'cd ~/hotlouddusty/hotlouddusty; python3 display/display.py'
fi
