#!/bin/env python3

import explorerhat
import keyboard
import time
from time import sleep

from curtsies import Input

class motors:
    def __init__(self):
        speed = 80
        inertia = 0.2
    
    def turn_left(self, speed):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.one.forward(speed)
            explorerhat.motor.two.forward(speed*0.5)
    
    def turn_right(self, speed):
        start = time.time()
        while (time.time()-start < self.inertia):
            explorerhat.motor.one.forward(speed*0.5)
            explorerhat.motor.two.forward(speed)
    
    def stop():
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    
    def keyboard(self):
        with Input(keynames='curses') as input_generator:
            for e in input_generator:
                if(e == 'w'):
                    start = time.time()
                    while (time.time()-start < self.inertia):
                        explorerhat.motor.forward(speed)
                if(e == 's'):
                    start = time.time()
                    while (time.time()-start < self.inertia):
                        explorerhat.motor.backwards(self.speed)
                if(e == 'a'):
                    turn_left(self.speed)
                if(e == 'd'):
                    turn_right(self.speed)
                else:
                    stop()
                


if __name__ == "__main__":
    motors.keyboard()

