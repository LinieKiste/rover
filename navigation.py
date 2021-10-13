#!/bin/env python3

from motors import motors
from colorsensor import colo

def nav(m, c):
    m.rotate(50)
    while True:
        m.rotate(30)
    while False:
        if(c.isRed()):
            m.forwards()
        else:
            m.stop()

if __name__ == "__main__":
    m = motors.motors(60)
    c = colo.colorSens()
    nav(m, c)
    # m.keyboard_unbuffered()

