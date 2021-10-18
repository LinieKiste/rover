#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import time


def findline(m):
    m.stop()


def nav(m, c):
    while True:
        if rpTut.distance() > 10:
            if c.is_red():
                print("red")
                m.forwards()
            else:
                print("not red")
                findline(m)
        else:
            m.stop()


if __name__ == "__main__":
    m = motors.motors(60)
    c = colo.colorSens()
    nav(m, c)
    # m.keyboard_unbuffered()
