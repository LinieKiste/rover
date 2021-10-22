#!/bin/env python3

import colo
import explorerhat
from explorerhat import motor
import time


def create_color_spectrum(color_sensor):
    for i in range(10):
        print("start moving")
        f = open("color_spectrum_red_"+str(i)+"_V02.txt", "w")
        color_sensor.get_color_from_sensor()
        f.write(str(color_sensor.get_color_rgb()))
        f.close()
        for _ in range(700):
            f = open("color_spectrum_red_"+str(i)+".txt", "a")
            color_sensor.get_color_from_sensor()
            f.write(", " + str(color_sensor.get_color_rgb()))
            f.close()
        duration_break = 30
        for c in range(duration_break):
            print(str(c) + " of " + str(duration_break))
            time.sleep(1)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    create_color_spectrum(color_sensor1)
