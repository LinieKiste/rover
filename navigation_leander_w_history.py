#!/bin/env python3

from distanceSensor import rpTut
from explorerhat import touch as button
from explorerhat import motor
import time
import simple_pid
import RPi.GPIO as GPIO


class PIDNavigatorRed:
    def __init__(self, very_slow=False):
        self.very_slow = very_slow
        self.base_speed = 41
        self.limit = 1
        self.motors_status = {motor.one: False, motor.two: False}
        self.pid_controller = simple_pid.PID(0.1, 10, 0, setpoint=50,
                                             output_limits=(-self.limit, self.limit))

    def kickstart(self, motors_list):
        for m in motors_list:
            m.forward(100)
            self.motors_status[m] = True
        time.sleep(0.02)

    def forward(self, motors_list, speed):
        for m in motors_list:
            if speed == 0:
                self.motors_status[m] = False
            elif not self.motors_status[m]:
                self.kickstart([m])
            m.forward(speed)

    def navigate(self, color_sensor):
        while True:
            if button.four.is_pressed() or GPIO.input(input_pin) == 1:
                self.forward([motor.one, motor.two], 0)
                break
            if self.very_slow:
                self.forward([motor.one, motor.two], 0)
            while rpTut.distance() < 10:  # avoid collisions
                self.forward([motor.one, motor.two], 0)
            control = self.pid_controller(color_sensor.get_color()[0])
            print(control)
            # left motor
            self.forward([motor.one], 0 if control == self.limit else self.base_speed - control)
            # right motor
            self.forward([motor.two], 0 if control == -self.limit else self.base_speed + control)


if __name__ == "__main__":
    # color_sensor1 = colo.ColorSensor()
    # pid_navigator_red = PIDNavigatorRed()
    # pid_navigator_red.navigate(color_sensor1)
    GPIO.setmode(GPIO.BCM)
    input_pin = 23
    GPIO.setup(input_pin, GPIO.IN)
    while True:
        print(GPIO.input(input_pin))
