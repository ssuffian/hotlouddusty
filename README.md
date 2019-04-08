# hotlouddusty

- hot: https://github.com/adafruit/Adafruit_Python_DHT
- loud: https://github.com/shichao-an/soundmeter
- dusty: https://github.com/ikalchev/py-sds011
- where: https://github.com/Knio/pynmea2, http://www.jillybunch.com/sharegps/nmea-usb-linux.html
- display: https://github.com/waveshare/e-Paper


## Install

	sudo apt update
	sudo raspi-config # Localization Options -> Time Zone -> Change Time Zone
        sudo raspi-config # Interfacing Options -> SPI -> Enable
	sudo apt install git portaudio19-dev python-dev alsa-utils libav-tools android-tools-adb screen python3-pip
        sudo apt-get install libjpeg-dev zlib1g-dev
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

## Display

For the display, it is using a [2.3 inch e-Paper HAT (D)](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(D)). Make sure to use the correct script from its github page. I used python3 and had to update a few things, such as the font (truetype font on raspberry pi zero is `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`. There were also a few tabs vs indent issues that had to be addressed in the files. Otherwise, `python main.py` from the [python3](https://github.com/waveshare/e-Paper/tree/master/2.13inch_e-paper_d_code/python3) folder worked.

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
	
