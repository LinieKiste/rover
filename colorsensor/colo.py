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

    def is_green(self):
        col = self.get_color_rgb()
        if 10 < col[0] < 20 and 30 < col[1] < 40 and 10 < col[2] < 20:
            return True
        return False

    def is_red(self):
        col = self.get_color_rgb()
        if 40 < col[0] < 60 and 0 < col[1] < 15 and 0 < col[2] < 15:
            return True
        return False

    def is_blue(self):
        col = self.get_color_rgb()
        if 0 < col[0] < 10 and 10 < col[1] < 20 and 25 < col[2] < 40:
            return True
        return False

    def is_white(self):
        col = self.get_color_rgb()
        if 10 < col[0] < 20 and 10 < col[1] < 20 and 10 < col[2] < 20:
            return True
        return False

    def show_color(self):
        print("RGB color as 8 bits per channel int: #{0:02X} or as a 3-tuple: {1}".format(self.get_color(),
                                                                                          self.get_color_rgb()))


if __name__ == "__main__":
    c = colorSens()
    color = c.get_color()
    while True:
        prev_color = color
        color = c.get_color()
        color_rgb = c.get_color_rgb()

        if prev_color != color:
            if not (c.is_red()) and not (c.is_blue()) and \
                    not (c.is_white()) and not (c.is_green()):
                print("RGB color as 8 bits per channel int: " +
                      "#{0:02X} or as a 3-tuple: {1}".format(
                          color, color_rgb))
