#!/bin/env python3

import board
import adafruit_tcs34725
import time


class colorSens:

    color = None
    color_rgb = None

    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)
        self.color = self.sensor.color
        self.get_color_from_sensor()
        self.get_color_rgb_from_sensor()

    # returns rgb as a hex value
    def get_color_from_sensor(self):
        self.color = self.sensor.color

    # returns (r, g, b) as a tuple
    def get_color_rgb_from_sensor(self):
        self.color_rgb = self.sensor.color_rgb_bytes

    def get_color_name(self, new_data_from_sensor=True):
        if new_data_from_sensor:
            self.get_color_from_sensor()
            self.get_color_rgb_from_sensor()
        if c.is_red(self.color_rgb):
            print("red")
        elif c.is_green(self.color_rgb):
            print("green")
        elif c.is_white(self.color_rgb):
            print("white")
        elif c.is_blue(self.color_rgb):
            print("blue")
        else:
            self.show_color()

    @staticmethod
    def is_green(col):
        if col[0] < 20 and 17 <= col[1] and col[2] < 20:
            return True
        return False

    @staticmethod
    def is_red(col):
        if 20 <= col[0] and col[1] < 20 and col[2] < 20:
            return True
        return False

    @staticmethod
    def is_blue(col):
        if col[0] < 20 and col[1] < 20 and 20 <= col[2]:
            return True
        return False

    @staticmethod
    def is_white(col):
        if col[0] < 20 and col[1] < 17 and col[2] < 20:
            return True
        return False

    def show_color(self):
        print("RGB color as 8 bits per channel int:" +
              " #{0:02X} or as a 3-tuple: {1}".format(self.color, self.color_rgb))


if __name__ == "__main__":
    c = colorSens()
    while True:
        c.get_color_name()

