#!/bin/env python3

import time
import explorerhat
import RPi.GPIO as GPIO

GPIO.setup(8, GPIO.OUT)

p = GPIO.PWM(8, 1000000)
p.start(1)

last = time.time()

def printandsave(self, val):
    global last
    print(time.time()-last)
    last = time.time()

while True:
    explorerhat.analog.one.changed(printandsave, 2)

