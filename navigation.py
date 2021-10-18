#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
import time


def nav(color_sensor):
    start = time.time()
    while True:
        while color_sensor.get_color_name() == "green":
            explorerhat.motor.one.forward(80)
            explorerhat.motor.two.forward(80)
        while color_sensor.get_color_name() == "red":
            explorerhat.motor.one.forward(80)
            explorerhat.motor.two.forward(-80)
        while color_sensor.get_color_name() == "blue":
            explorerhat.motor.one.forward(-80)
            explorerhat.motor.two.forward(80)
        counter = 0
        while color_sensor.get_color_name() == "white" and counter < 100:
            explorerhat.motor.one.forward(80)
            explorerhat.motor.two.forward(80)
        while color_sensor.get_color_name() == "white":
            explorerhat.motor.one.forward(0)
            explorerhat.motor.two.forward(0)


if __name__ == "__main__":
    color_sensor = colo.ColorSensor()
    nav(color_sensor)
