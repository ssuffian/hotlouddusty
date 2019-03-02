# hotlouddusty

- loud: https://github.com/shichao-an/soundmeter
- dusty: https://github.com/ikalchev/py-sds011
- where: https://github.com/Knio/pynmea2, http://www.jillybunch.com/sharegps/nmea-usb-linux.html


## Install

	sudo apt update
	sudo raspi-config # Localization Options -> Time Zone -> Change Time Zone
	sudo apt install git portaudio19-dev python-dev alsa-utils libav-tools android-tools-adb screen python3-pip
	git clone git@github.com:ssuffian/hotlouddusty.git
	pip3 install -r requirements.txt 
        crontab crontab.txt

## Hot

You need to install a DHT22/AM2302 temperature sensor. It is currently set up for the data pin to be on pin 23.
	
## Audio

Go into alsa.conf and change the 0's to 1's for the following lines (`defaults.ctl card 0` and `defaults.pcm.card 0`):

	sudo vim /usr/share/alsa/alsa.conf
	defaults.ctl.card 1
    	defaults.pcm.card 1

## Dusty

This is the module that specifically requires python3. The others could be run on python2.7, but for consistently everything is being run on python3
	
	cd lib/py-sds011
	git submodule init 
	git submodule update
	sudo python3 setup.py install

## Where


If it is a new device, you must go on the phone and authorize the device.

### Debugging

This [page](http://www.jillybunch.com/sharegps/nmea-usb-linux.html) is helpful with debugging (and was how I figured out how to get it setup.

	sudo apt install gpsd netcat


## Other

To save crontab to file:
        
	crontab -l > crontab.txt
        
To load crontab from file:

	crontab crontab.txt

## Vim
	sudo apt install vim
	sudo update-alternatives --config editor 

Select vim.basic
	
