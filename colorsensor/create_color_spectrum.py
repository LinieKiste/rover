#!/bin/env python3

import colo
import explorerhat
from explorerhat import motor
import time


def create_color_spectrum(color_sensor):
    f = open("color_spectrum_red.txt", "a")
    for _ in range(200000):
        color_sensor.get_color_from_sensor()
        f.write(str(color_sensor.get_color_rgb())+", ")
        time.sleep(0.001)
    color_sensor.get_color_from_sensor()
    f.write(str(color_sensor.get_color_rgb()))
    f.close()


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    create_color_spectrum(color_sensor1)
