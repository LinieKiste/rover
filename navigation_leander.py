#!/bin/env python3

from colorsensor import colo
from distanceSensor import rpTut
from explorerhat import motor
import time
import simple_pid
from RPi import GPIO


class CollisionAndEmergencyBreakHandler:
    def __init__(self, emergency_break_pin=22):
        GPIO.setup(emergency_break_pin, GPIO.IN)
        self.emergency_break_pin = emergency_break_pin

    def check_for_emergency_break(self):
        if GPIO.input(self.emergency_break_pin) == 1:
            motor.stop()
            print("emergency break detected")
            return True
        return False

    def check_for_collision_and_emergency_break(self):
        while rpTut.distance() < 10:  # avoid collisions
            motor.stop()
            if self.check_for_emergency_break():
                break
        return self.check_for_emergency_break()


class PIDNavigatorRed:
    def __init__(self):
        self.caebh = CollisionAndEmergencyBreakHandler()
        self.color_sensor = colo.ColorSensor()
        self.limit = 24
        self.setpoint = 40
        self.pid_controller = \
            simple_pid.PID(4, 1, 0.01, setpoint=self.setpoint,
                           output_limits=(-self.limit, self.limit))

    def navigate(self):
        # move the rover to the right side of the line
        # motor.two.backward(100)
        # time.sleep(0.3)
        # motor.forward(100)
        # time.sleep(0.15)
        motor.stop()
        run_time = 0
        while not self.caebh.check_for_collision_and_emergency_break():
            motor.stop()
            if self.color_sensor.get_color()[0] <= 16 or \
                    self.color_sensor.get_color()[0] > 70:
                motor.backward(100)
                time.sleep(run_time)
                run_time = 0.03
            control = self.pid_controller(self.color_sensor.get_color()[0])
            print("control: ", control)
            motor.one.forward(66 - control)  # left motor
            motor.two.forward(66 + control)  # right motor
            time.sleep(run_time)
            run_time += 0.01
        return False


if __name__ == "__main__":
    pid_navigator_red_main = PIDNavigatorRed()
    pid_navigator_red_main.navigate()
