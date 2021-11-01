#!/bin/python3

import explorerhat
from explorerhat import motor
import time
from camera import Camera
import tty
import sys
import termios
import atexit

forward = 70
rot = 50
offset = 15

def rotate(timespan):
    x = 80
    motor.one.forward(x)
    motor.two.backward(x)
    time.sleep(.03)
    x = rot
    motor.one.forward(x)
    motor.two.backward(x)
    time.sleep(timespan)

def kickstart(left):
    x = 80
    if left:
        motor.one.forward(x)
        motor.two.backward(x)
    else:
        motor.one.backward(x)
        motor.two.forward(x)
    time.sleep(.03)


def find(c):
    while True:
        motor.stop()
        start = time.time()
        timer = 0
        data = None
        while timer < .7:
            try:
                data = c.scan_qr_code()
            except:
                print("error, exiting manually...")
                exit()
            if data is not None:
                instructions(data + '.txt')
                break
            timer = time.time() - start

        if data is not None:
            return data
            break
        else:
            rotate(.2)

def instructions(fname):
    with open(fname, 'r') as f:
        lines = f.read().split('\n')
        for instr in lines:
            (key, t) = instr.split(' ')
            t = float(t)
            start = time.time()
            while time.time() - start < t:
                if key == 'd':
                    kickstart(True)
                    motor.one.forward(rot)
                    motor.two.backward(rot)
                if key == 'a':
                    kickstart(False)
                    motor.one.backward(rot)
                    motor.two.forward( rot)
                if key == 'w':
                    motor.one.forward(forward)
                    motor.two.forward(forward+offset)
            motor.stop()
            time.sleep(.3)


def keyboard(fname):
    commands = ""
    orig_settings = termios.tcgetattr(sys.stdin)
    def exit_handler():
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)

    atexit.register(exit_handler)

    tty.setcbreak(sys.stdin)
    t = 0
    x = 0
    print("starting")
    while x != chr(27):
        x = sys.stdin.read(1)[0]
        start = time.time()
        if x == 'd':
            kickstart(True)
            motor.one.forward(rot)
            motor.two.backward(rot)
            checkforspace()
            t = time.time() - start
            commands += "d " + str(t) + "\n"
        if x == 'a':
            kickstart(False)
            motor.one.backward(rot)
            motor.two.forward( rot)
            checkforspace()
            t = time.time() - start
            commands += "a " + str(t) + "\n"
        if x == 'w':
            motor.one.forward(forward)
            motor.two.forward(forward+offset)
            checkforspace()
            t = time.time() - start
            commands += "w " + str(t) + "\n"
        print(f"{x} took {t} seconds")
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
    with open(fname, 'w') as f:
        f.write(commands)

def checkforspace():
    while True:
        x = sys.stdin.read(1)[0]
        if x == chr(32):
            motor.stop()
            break

if __name__ == '__main__':
    c = Camera()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'r':
            print('recording commands...')
            keyboard(sys.argv[2])
    else:
        print('looking for qr code...')
        print(f"found data {find(c)}")
    print('exiting...')
