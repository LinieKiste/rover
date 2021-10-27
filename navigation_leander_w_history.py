#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time
import simple_pid


class Navigator:
    def __init__(self):
        self.base_speed = 25
        self.limit = 0.5
        self.motors_status = {motor.one: False, motor.two: False}
        self.pid_controller = simple_pid.PID(0.1, 0.2, 0, setpoint=60,
                                             output_limits=(-self.limit, self.limit))

    def kickstart(self, motors_list):
        for m in motors_list:
            m.forward(100)
            self.motors_status[m] = True
        time.sleep(0.01)

    def forward(self, motors_list, speed):
        for m in motors_list:
            if speed == 0:
                self.motors_status[m] = False
            elif not self.motors_status[m]:
                self.kickstart([m])
            m.forward(speed)

    def navigate(self, color_sensor):
        while True:
            while rpTut.distance() < 10:  # avoid collisions
                self.forward([motor.one, motor.two], 0)
            control = self.pid_controller(color_sensor.get_color()[0])
            print(control)
            # left motor
            self.forward([motor.one], 0 if control == self.limit else self.base_speed - control)
            # right motor
            self.forward([motor.two], 0 if control == -self.limit else self.base_speed + control)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    navigator1 = Navigator()
    navigator1.navigate(color_sensor1)
