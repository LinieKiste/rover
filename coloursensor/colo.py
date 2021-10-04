#!/bin/env python3

import board
import adafruit_tcs34725
import time

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

color = sensor.color
while True:
    prev_color = color
    color = sensor.color
    color_rgb = sensor.color_rgb_bytes

    if(prev_color != color):
        print("RGB color as 8 bits per channel int: #{0:02X} or as a 3-tuple: {1}".format(
            color, color_rgb
            )
        )



