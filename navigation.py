#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import time

def nav(m, c):
    print("Hello")
    while True:
        print(rpTut.distance())
        print(f"distance = {rpTut.distance()} cm")
        time.sleep(0.3)
    while True:
        if rpTut.distance() > 10:
            if(c.isRed()):
                m.forwards()
            else:
                m.stop()
        else:
            m.stop()

if __name__ == "__main__":
    m = motors.motors(60)
    c = colo.colorSens()
    nav(m, c)
    # m.keyboard_unbuffered()

