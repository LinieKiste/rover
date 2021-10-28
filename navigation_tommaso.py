#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
import explorerhat
from explorerhat import motor
import time
import simple_pid


class Navigator:

    def navigation_tommaso(self, color_sensor):
        while True:
            control = color_sensor.get_color()[0] 
            print(control)
            while rpTut.distance() < 10: #avoid collisions
                motor.stop()
            if control < 50:
                motor.one.forward(100)
            elif 50 <= control < 80:
                motor.forward(100)
            else: 
                motor.two.forward(100)
            time.sleep(0.03)
            motor.stop()

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

    def navigation_leander(self, color_sensor):
        while True:
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
    color_sensor = colo.ColorSensor()
    navigator = Navigator()
    while True:
        if explorerhat.touch.one.is_pressed():
            print("Button 1 pressed: running Tommaso's program")
            navigator.navigation_tommaso(color_sensor)
        elif explorerhat.touch.two.is_pressed():
            print("Button 2 pressed: running Leander's program")
            navigator.navigation_leander(color_sensor)

