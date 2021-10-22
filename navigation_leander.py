#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time
import simple_pid



def nav(color_sensor):
    explorerhat.motor.forward(100)
    time.sleep(0.01)
    pid_controller = simple_pid.PID(10, 0, 0, setpoint=0)
    while True:
        color_sensor.get_color_from_sensor()
        red_value = color_sensor.get_color_rgb()[0]
        control = pid_controller(red_value/120 - 0.6)
        print(control)
        base_throttle = 50
        offset = 4.5
        left = base_throttle - offset - control
        right = base_throttle + offset + control

        if left >= 0:
            explorerhat.motor.one.forward(left)
        else:
            explorerhat.motor.one.backward(abs(left))
        if right >= 0:
            explorerhat.motor.two.forward(right)
        else:
            explorerhat.motor.two.backward(abs(right))


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
