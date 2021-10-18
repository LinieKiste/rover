#!/bin/env python3

import board
import adafruit_tcs34725


class ColorSensor:

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

    def get_color_name(self, get_new_data_from_sensor=True):
        # print(self.color_rgb)
        if get_new_data_from_sensor:
            self.get_color_from_sensor()
            self.get_color_rgb_from_sensor()

        if self.is_red():
            return "red"
        elif self.is_green():
            return "green"
        elif self.is_white():
            return "white"
        elif self.is_blue():
            return "blue"
        elif self.is_between_green_and_blue():
            return "between_green_and_blue"
        else:
            return "no_color_found"

    def is_between_green_and_blue(self):
        return self.color_rgb[0] < 10 and 10 <= self.color_rgb[1] and 10 <= self.color_rgb[2]

    def is_green(self):
        return self.color_rgb[0] < 20 and 20 <= self.color_rgb[1] and self.color_rgb[2] < 20

    def is_red(self):
        return 20 <= self.color_rgb[0] and self.color_rgb[1] < 20 and self.color_rgb[2] < 20

    def is_blue(self):
        return self.color_rgb[0] < 20 and self.color_rgb[1] < 20 and 20 <= self.color_rgb[2]

    def is_white(self):
        return self.color_rgb[0] < 20 and self.color_rgb[1] < 20 and self.color_rgb[2] < 20

    def show_color(self):
        print("RGB color as 8 bits per channel int:" +
              " #{0:02X} or as a 3-tuple: {1}".format(self.color, self.color_rgb))


if __name__ == "__main__":
    color_sensor = ColorSensor()
    while True:
        print(color_sensor.get_color_name())
