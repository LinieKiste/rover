#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time
import simple_pid


def kickstart(left_motor=True, right_motor=True):
    kickstart_time = 0.01
    kickstart_speed = 100
    if left_motor:
        motor.one.forward(kickstart_speed)
        time.sleep(kickstart_time)
    if right_motor:
        motor.two.forward(kickstart_speed)
        time.sleep(kickstart_time)

def nav(color_sensor):
    use_offset = False

    # increase this variable, if it dies to often
    base_speed = 50
    limit = 5
    offset = 0
    if use_offset:
        offset = 4.5
        limit = 10

    right_motor_runing = False
    left_motor_runing = False
    pid_controller = simple_pid.PID(0.5, 1, 1, setpoint=50, output_limits=(-limit, limit))

    while True:
        while rpTut.distance() < 10:
             right_motor_runing = False
             left_motor_runing = False
             motor.stop()

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



if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    nav(color_sensor1)
