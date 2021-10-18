#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
import time

counter = 0

def findline(m):
    m.stop()
    if counter < 9:
        m.rotate(0.1)
        time.sleep(1)
    else:
        m.rotate(-40)
        time.sleep(1)

def nav(m, c):
    while True:
        if rpTut.distance() > 10:
            if c.is_red():
                counter = 0
                explorerhat.motor.forward(80)
            else:
                m.stop()
                explorerhat.motor.one.forward(0)
                explorerhat.motor.two.forward(80)
                # findline(m)
        else:
            m.stop()


if __name__ == "__main__":
    m = motors.motors(50)
    c = colo.colorSens()
    nav(m, c)
    # m.keyboard_unbuffered()
