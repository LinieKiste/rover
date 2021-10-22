#!/bin/env python3

import colo
import explorerhat
from explorerhat import motor
import time


def create_color_spectrum(color_sensor):
    for i in range(5):
        motor.forward(100)
        time.sleep(0.1)
        motor.forward(50)
        f = open("color_spectrum_red_"+str(i)+".txt", "w")
        color_sensor.get_color_from_sensor()
        f.write(str(color_sensor.get_color_rgb()))
        f.close()
        for _ in range(100000):
            f = open("color_spectrum_red_"+str(i)+".txt", "a")
            color_sensor.get_color_from_sensor()
            f.write(", " + str(color_sensor.get_color_rgb()))
            f.close()
        motor.stop()
        time.sleep(5)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    create_color_spectrum(color_sensor1)
