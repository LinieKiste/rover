#!/bin/python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut

import simple_pid
import time
import explorerhat

def go(color_sensor):
    motor = explorerhat.motor
    limit = 10
    throttle = 40
    controller = simple_pid.PID(0.2, 0.2, 0, setpoint=40, output_limits=(-limit, limit))
    
    # kickstart
    motor.forward(100)
    time.sleep(0.01)
    while True:
        if rpTut.distance() < 10:
            break

        steering = controller(color_sensor.get_color()[0])
        motor.one.forward(throttle + steering)
        motor.two.forward(throttle - steering)


if __name__ == '__main__':
    sens = colo.ColorSensor()
    go(sens)

