# hotlouddusty

- loud: https://github.com/shichao-an/soundmeter
- dusty: https://github.com/ikalchev/py-sds011
- where: https://github.com/Knio/pynmea2

## Install

	sudo apt update
	sudo apt install git portaudio19-dev python-dev alsa-utils libav-tools android-tools-adb screen
	git clone 
	pip install -r requirements.txt 
        crontab crontab.txt
	
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
