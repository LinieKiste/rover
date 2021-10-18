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

    def is_green(self, col):
        # col = self.get_color_rgb()
        if col[0] < 25 and 25 < col[1] and col[2] < 25:
            return True
        return False

    def is_red(self, col):
        # col = self.get_color_rgb()
        if 25 < col[0] and col[1] < 25 and col[2] < 25:
            return True
        return False

    def is_blue(self, col):
        # col = self.get_color_rgb()
        if col[0] < 25 and col[1] < 25 and 25 < col[2]:
            return True
        return False

    def is_white(self, col):
        # col = self.get_color_rgb()
        if col[0] < 25 and col[1] < 25 and col[2] < 25:
            return True
        return False

    def show_color(self):
        print("RGB color as 8 bits per channel int: #{0:02X} or as a 3-tuple: {1}".format(self.get_color(),
                                                                                          self.get_color_rgb()))


if __name__ == "__main__":
    c = colorSens()
    while True:
        color = c.get_color()
        color_rgb = c.get_color_rgb()
        if c.is_red(color_rgb):
            print("red")
        elif c.is_green(color_rgb):
            print("green")
        elif c.is_white(color_rgb):
            print("white")
        elif c.is_blue(color_rgb):
            print("blue")
        else:
            print("RGB color as 8 bits per channel int: " +
                  "#{0:02X} or as a 3-tuple: {1}".format(color, color_rgb))

