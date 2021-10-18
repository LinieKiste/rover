#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
import time


def nav(m, c):
    while True:
        while c.is_red():
            explorerhat.motor.one.forward(0)
            explorerhat.motor.two.forward(80)


if __name__ == "__main__":
    m = motors.motors(50)
    c = colo.colorSens()
    nav(m, c)
    # m.keyboard_unbuffered()
