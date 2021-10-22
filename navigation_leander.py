#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time
import simple_pid

def kickstart(left_motor=True, right_motor=True):
    if left_motor:
        motor.one.forward(100)
        time.sleep(0.01)
    if right_motor:
        motor.two.forward(100)
        time.sleep(0.01)

def nav(color_sensor):
    use_offset = False

    # increase this variable, if it dies to often
    base_speed = 25
    limit = 0.5
    offset = 0
    if use_offset:
        offset = 4.5
        limit = 10

    right_motor_runing = False
    left_motor_runing = False
    pid_controller = simple_pid.PID(0.1, 0.2, 0, setpoint=60, output_limits=(-limit, limit))

    while True:
        control = pid_controller(color_sensor.get_color()[0])
        print(control)

        # left motor
        if control == limit:
            left_motor_runing = False
            motor.one.stop()
        else:
            if not left_motor_runing:
                kickstart(True, False)
                left_motor_runing = True
            motor.one.forward(base_speed - offset - control)

        # right motor
        if control == -limit:
            right_motor_runing = False
            motor.two.stop()
        else:
            if not right_motor_runing:
                kickstart(False, True)
                right_motor_runing = True
            motor.two.forward(base_speed + offset + control)
    motor.stop()




if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
