#!/bin/env python3

import board
import adafruit_tcs34725
import time

class colorSens:
    
    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)
        self.color = self.sensor.color

    # returns rgb as a hex value
    def get_color(self):
        return self.sensor.color

    # returns (r, g, b) as a tuple
    def get_color_rgb(self):
        return self.sensor.color_rgb_bytes

    def isRed(self):
        col = self.get_color_rgb()
        if(col[0] > 30 and col[1] < 15 and col[2] < 15):
            return True
        return False

    def show_color(self):
        print("RGB color as 8 bits per channel int: #{0:02X} or as a 3-tuple: {1}".format(self.get_color(), self.get_color_rgb()))

if __name__ == "__main__":
    c = colorSens()
    color = c.get_color()
    while True:
        prev_color = color
        color = c.get_color()
        color_rgb = c.get_color_rgb()

        if(prev_color != color):
            print("RGB color as 8 bits per channel int: #{0:02X} or as a 3-tuple: {1}".format(
                color, color_rgb
                )
            )

        # if(color_rgb[0]>50):
        #     print("RED")
        
        
