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
                m.forwards()
            else:
                findline(m)
        else:
            m.stop()
        time.sleep(0.3)


if __name__ == "__main__":
    m = motors.motors(60)
    c = colo.colorSens()
    nav(m, c)
    # m.keyboard_unbuffered()
