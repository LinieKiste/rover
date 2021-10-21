#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time



def nav(color_sensor):
    while True:
        collect_colors()

if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
