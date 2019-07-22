#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
from datetime import datetime
import epd2in13d
import os
from PIL import Image,ImageDraw,ImageFont
import time
import traceback


def _slice_str_dt(dt):
    return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f').strftime('%H:%M:%S')


def display():
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
            data = get_latest_data()
            loud = '{} db, {}'.format(data['loud']['db'], _slice_str_dt(data['loud']['datetime']))
            dusty = '{} pm2.5, {}'.format(data['dusty']['pm2.5'], _slice_str_dt(data['dusty']['datetime']))
            #time_draw.text((10, 5), time.strftime( 'Hot     %H:%M:%S'), font = font18, fill = 0)
            time_draw.text((10, 25), loud, font = font18, fill = 0)
            time_draw.text((10, 45), dusty, font = font18, fill = 0)
            #time_draw.text((10, 65), time.strftime('Where %H:%M:%S'), font = font18, fill = 0)
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


def get_latest_data():
    data = {}
    for key in ['hot', 'loud', 'dusty']:
        filename = '/home/pi/hotlouddusty/data/{}-current.csv'.format(key)
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                reader = csv.DictReader(f)
                value = [row for row in reader][0]
                data[key] = value
    return data


if __name__ == '__main__':
    display()
