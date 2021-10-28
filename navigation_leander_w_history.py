#!/bin/env python3

from colorsensor import colo
from distanceSensor import rpTut
from explorerhat import touch as button
from explorerhat import motor
import time
import simple_pid
from RPi import GPIO


def stop_motors(navigator=None):
    if navigator:
        navigator.forward([motor.one, motor.two], 0)
    else:
        motor.stop()


class CollisionAndEmergencyBreakHandler:
    def __init__(self, emergency_break_pin=22):
        GPIO.setup(emergency_break_pin, GPIO.IN)
        self.emergency_break_pin = emergency_break_pin

    def check_for_emergency_break(self, navigator=None):
        if GPIO.input(self.emergency_break_pin) == 1:
            stop_motors(navigator)
            print("emergency break detected")
            return True
        return False

    def check_for_collision_and_emergency_break(self, navigator=None):
        while rpTut.distance() < 10:  # avoid collisions
            stop_motors(navigator)
            if self.check_for_emergency_break(navigator):
                break
        return self.check_for_emergency_break(navigator)


class PIDNavigatorRedSimple:
    def __init__(self, color_sensor, collision_and_emergency_break_handler):
        self.caebh = collision_and_emergency_break_handler
        self.color_sensor = color_sensor

    def navigate(self):
        while True:
            if self.caebh.check_for_collision_and_emergency_break(self):
                break
            if self.color_sensor.get_color()[0] > 40:
                motor.one.forward(50)
            else:
                motor.one.stop()
            if self.color_sensor.get_color(True, False)[0] < 60:
                motor.two.forward(50)
            else:
                motor.two.stop()


class PIDNavigatorRed:
    def __init__(self, color_sensor, collision_and_emergency_break_handler, very_slow=False):
        self.caebh = collision_and_emergency_break_handler
        self.color_sensor = color_sensor
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

    def navigate(self):
        while True:
            if self.caebh.check_for_collision_and_emergency_break(self):
                break
            control = self.pid_controller(color_sensor.get_color()[0])
            print("control: ", control)
            # left motor
            self.forward([motor.one], 0 if control == self.limit else self.base_speed - control)
            # right motor
            self.forward([motor.two], 0 if control == -self.limit else self.base_speed + control)


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    caebh = CollisionAndEmergencyBreakHandler()
    pid_navigator_red = PIDNavigatorRed(color_sensor1, caebh)
    pid_navigator_red_simple = PIDNavigatorRedSimple(color_sensor1, caebh)
    pid_navigator_red_simple.navigate()
