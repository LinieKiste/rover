#!/bin/env python3

import explorerhat
import keyboard
import time
from time import sleep

from curtsies import Input

class motors:
    def __init__(self):
        self.speed = 80
        self.inertia = 0.4

    def __init__(self, sp):
        self.speed = sp
        self.inertia = 0.4

    def set_speed(self, new_speed):
        self.speed = new_speed

    def rotate(self, a):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.one.forward(a)
            explorerhat.motor.two.backwards(a)
    
    def forwards(self):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.forward(self.speed)
    
    def backwards(self):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.backwards(self.speed)
    
    def turn_left(self):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.one.forward(self.speed)
            explorerhat.motor.two.forward(self.speed*0.5)
    
    def turn_right(self):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.one.forward(self.speed*0.5)
            explorerhat.motor.two.forward(self.speed)
    
    def stop(self):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    
    def keyboard_unbuffered(self):
        import tty
        import sys
        import termios
        import atexit
    
        orig_settings = termios.tcgetattr(sys.stdin)
    
        def exit_handler():
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    
        atexit.register(exit_handler)
    
        tty.setcbreak(sys.stdin)
        input = 0
        while input != chr(27): # ESC
            x = sys.stdin.read(1)[0]
            if(x == 'w'):
                self.forwards  ()
            if(x == 's'):
                self.backwards ()
            if(x == 'a'):
                self.turn_left ()
            if(x == 'd'):
                self.turn_right()
            if(x == chr(27)):
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
            else:
                self.stop()
    
    
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
    m = motors()
    m.keyboard_unbuffered()
    # while True:
    #     if time.time()-first < 5:
    #         turn_left(80)
    #     else:
    #         turn_right(80)

