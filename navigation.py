#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time



def nav(color_sensor):
    while True:
        while color_sensor.get_color_name() == "green":
            motor.forward(60)
        while color_sensor.get_color_name() == "red":
            motor.two.forward(40)
            motor.one.forward(60)
            time.sleep(0.01)
            motor.two.forward(60)
            motor.two.forward(40)
        while color_sensor.get_color_name() == "blue":
            motor.one.forward(40)
            motor.two.forward(60)
            # motor.two.stop()
            # time.sleep(0.01)
            # break
        counter = 0
        while color_sensor.get_color_name() == "white" and counter < 10:
            motor.forward(60)
            counter+=1
        while color_sensor.get_color_name() == "white":
            motor.backward(60)
        # counter = 0
        # while color_sensor.get_color_name() == "no_color_found" and counter < 100:
            # motor.forward(60)
            # counter+=1
        # while color_sensor.get_color_name() == "no_color_found":
            # motor.backward(60)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
