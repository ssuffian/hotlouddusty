# hotlouddusty

- loud: https://github.com/shichao-an/soundmeter
- dusty: https://github.com/ikalchev/py-sds011
- where: https://github.com/Knio/pynmea2

## Install

	sudo apt update
	sudo apt install git portaudio19-dev python-dev alsa-utils libav-tools android-tools-adb screen python-pip
	git clone git@github.com:ssuffian/hotlouddusty.git
	pip install -r requirements.txt 
        crontab crontab.txt
	
## Audio

Go into alsa.conf and change the 0's to 1's for the following lines (`defaults.ctl card 0` and `defaults.pcm.card 0`):

	sudo vim /usr/share/alsa/alsa.conf
	defaults.ctl.card 1
    	defaults.pcm.card 1

## Dusty
	
	cd lib/py-sds011
	git submodule init 
	git submodule update
	sudo python setup.py install

## Where

If it is a new device, you must go on the phone and authorize the device.

## Other

To save crontab to file:
        
	crontab -l > crontab.txt
        
To load crontab from file:

	crontab crontab.txt

## Vim
	sudo apt install vim
	sudo update-alternatives --config editor 

Select vim.basic
	
