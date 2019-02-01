# bm_pi_zero_sensors

- loud: https://github.com/shichao-an/soundmeter
- dusty: https://github.com/ikalchev/py-sds011
- where: https://github.com/Knio/pynmea2

## Install

	sudo apt-get update
	sudo apt-get install portaudio19-dev python-dev alsa-utils libav-tools
	pip install -r requirements.txt 
	
## Audio

Go into alsa.conf and change the 0's to 1's for the following lines:

	sudo vim /usr/share/alsa/alsa.conf
	defaults.ctl.card 0
    	defaults.pcm.card 0
