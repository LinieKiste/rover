#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat.motor as motor
import time


def nav(color_sensor):
    while True:
        while color_sensor.get_color_name() == "green":
            motor.forward(80)
        while color_sensor.get_color_name() == "red":
            motor.one.forward(80)
            motor.two.forward(-80)
        while color_sensor.get_color_name() == "blue":
            motor.one.forward(-80)
            motor.two.forward(80)
        counter = 0
        while color_sensor.get_color_name() == "white" and counter < 100:
            motor.forward(80)
        while color_sensor.get_color_name() == "white":
            motor.stop()
        counter = 0
        while color_sensor.get_color_name() == "no_color_found" and counter < 100:
            motor.forward(80)
        while color_sensor.get_color_name() == "no_color_found":
            motor.stop()


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
