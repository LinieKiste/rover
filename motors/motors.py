#!/bin/env python3

import explorerhat
import keyboard
import time
from time import sleep

from curtsies import Input

speed = 80
inertia = 0.4

def forwards(speed):
    start = time.time()
    while (time.time()-start < inertia):
        explorerhat.motor.forward(speed)

def backwards(speed):
    start = time.time()
    while (time.time()-start < inertia):
        explorerhat.motor.backwards(speed)

def turn_left(speed):
    start = time.time()
    while (time.time()-start < inertia):
        explorerhat.motor.one.forward(speed)
        explorerhat.motor.two.forward(speed*0.5)

def turn_right(speed):
    start = time.time()
    while (time.time()-start < inertia):
        explorerhat.motor.one.forward(speed*0.5)
        explorerhat.motor.two.forward(speed)

def stop():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.stop()

def keyboard_unbuffered():
    import tty
    import sys
    import termios

    orig_settings = termios.tcgetattr(sys.stdin)

    tty.setcbreak(sys.stdin)
    input = 0
    while input != chr(27): # ESC
        x = sys.stdin.read(1)[0]
        if(e == 'w'):
            forwards(speed)
        if(e == 's'):
            backwards(speed)
        if(e == 'a'):
            turn_left(speed)
        if(e == 'd'):
            turn_right(speed)
        else:
            stop()


def keyboard():
    with Input(keynames='curses') as input_generator:
        prev = None
        for e in input_generator:
            if e != prev:
                prev = e
                if(e == 'w'):
                    forwards(speed)
                if(e == 's'):
                    backwards(speed)
                if(e == 'a'):
                    turn_left(speed)
                if(e == 'd'):
                    turn_right(speed)
                else:
                    stop()
                


if __name__ == "__main__":
    # kickstart()
    keyboard()
    # while True:
    #     if time.time()-first < 5:
    #         turn_left(80)
    #     else:
    #         turn_right(80)

