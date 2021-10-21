#!/bin/env python3

import colo
import explorerhat
from explorerhat import motor
import time


def create_color_spectrum(color_sensor):
    for _ in range(10000):
        color_sensor.get_color_from_sensor()
        f = open("color_spectrum.txt", "a")
        f.write(str(color_sensor.get_color_rgb()) + ",\n")
        f.write(",")
        f.close()
        time.sleep(0.01)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    create_color_spectrum(color_sensor1)
