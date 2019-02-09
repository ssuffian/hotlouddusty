# hotlouddusty

- loud: https://github.com/shichao-an/soundmeter
- dusty: https://github.com/ikalchev/py-sds011
- where: https://github.com/Knio/pynmea2

## Install

	sudo apt-get update
	sudo apt-get install portaudio19-dev python-dev alsa-utils libav-tools
        sudo apt install android-tools-adb screen
	pip install -r requirements.txt 
	
## Audio

Go into alsa.conf and change the 0's to 1's for the following lines:

	sudo vim /usr/share/alsa/alsa.conf
	defaults.ctl.card 0
    	defaults.pcm.card 0

## Dusty

	cd lib/py-sds011
	sudo python setup.py install

## Where

If it is a new device, you must go on the phone and authorize the device.

## Other

        crontab -l > crontab.txt
        crontab crontab.txt
