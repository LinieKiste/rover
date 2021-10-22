#!/bin/env python3

import colo
import explorerhat
from explorerhat import motor
import time


def create_color_spectrum(color_sensor):
    motor.forward(100)
    time.sleep(0.03)
    motor.forward(40)
    time.sleep(5)
    motor.stop()
    return
    for _ in range(20000):
        f = open("color_spectrum_red.txt", "a")
        color_sensor.get_color_from_sensor()
        f.write(str(color_sensor.get_color_rgb())+", ")
        time.sleep(0.001)
        f.close()
    f = open("color_spectrum_red.txt", "a")
    color_sensor.get_color_from_sensor()
    f.write(str(color_sensor.get_color_rgb()))
    f.close()


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    create_color_spectrum(color_sensor1)
