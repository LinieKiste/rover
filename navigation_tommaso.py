#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time


def nav(color_sensor):
    speedFAST = 50
    speedSLOW = 30

    while True:
        if rpTut.distance() < 10:
            motor.stop()
            break
        while color_sensor.get_color_name() == "green":
            motor.forward(speedFAST)
        while color_sensor.get_color_name() == "red":
            # should turn left
            motor.one.forward(speedFAST)
            motor.two.forward(speedSLOW)
        while color_sensor.get_color_name() == "blue":
            # should turn right
            motor.one.forward(speedSLOW)
            motor.two.forward(speedFAST)
        counter = 0
        while color_sensor.get_color_name() == "white" and counter < 3:
            motor.forward(speedFAST)
            counter+=1
        while color_sensor.get_color_name() == "white":
            motor.backward(speedFAST)
        # counter = 0
        # while color_sensor.get_color_name() == "no_color_found" and counter < 100:
            # motor.forward(speedFAST)
            # counter+=1
        # while color_sensor.get_color_name() == "no_color_found":
            # motor.backward(speedFAST)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
