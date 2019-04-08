#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in13d
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd2in13d.EPD()
    epd.init()
    epd.Clear(0xFF)
    font_str = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    font18 = ImageFont.truetype(font_str, 18)
    time_image = Image.new('1', (epd2in13d.EPD_HEIGHT, epd2in13d.EPD_WIDTH), 255)
    time_draw = ImageDraw.Draw(time_image)
    while (True):
        rect_size = (10, 5, 200, 200)
        time_draw.rectangle(rect_size, fill = 255)
        time_draw.text((10, 5), time.strftime( 'Hot     %H:%M:%S'), font = font18, fill = 0)
        time_draw.text((10, 25), time.strftime('Loud   %H:%M:%S'), font = font18, fill = 0)
        time_draw.text((10, 45), time.strftime('Dusty  %H:%M:%S'), font = font18, fill = 0)
        time_draw.text((10, 65), time.strftime('Where %H:%M:%S'), font = font18, fill = 0)
        time_draw.text((10, 85), time.strftime('%H:%M:%S'), font = font18, fill = 0)
        newimage = time_image.crop(list(rect_size))
        time_image.paste(newimage, (10,5))  
        epd.DisplayPartial(epd.getbuffer(time_image))
        
        
except (KeyboardInterrupt, SystemExit):
    epd.Clear(0xFF)
    epd.sleep()
except Exception as e:
    print('traceback.format_exc():\n%s',traceback.format_exc())
    exit()

