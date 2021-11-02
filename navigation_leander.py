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
        self.limit = 10
        self.setpoint = 25
        self.pid_controller = \
            simple_pid.PID(1, 2, 0.01, setpoint=self.setpoint,
                           output_limits=(-self.limit, self.limit))

    def navigate(self):
        # move the rover to the right side of the line
        # motor.two.backward(100)
        # time.sleep(0.3)
        # motor.forward(100)
        # time.sleep(0.15)
        motor.stop()
        timer = 2
        while not self.caebh.check_for_collision_and_emergency_break():
            # motor.stop()
            for i in range(timer):
                if self.color_sensor.get_color()[0] <= 16 or \
                        self.color_sensor.get_color()[0] > 70:
                    motor.backward(100)
                    time.sleep(0.01)
                    if timer >= 5:
                        timer -= 3
                    break
                time.sleep(0.001)
            motor.stop()
            control = self.pid_controller(self.color_sensor.get_color()[0])
            print("control: ", control)
            motor.one.forward(75 - control)  # left motor
            motor.two.forward(75 + control)  # right motor
            timer += 1



if __name__ == "__main__":
    pid_navigator_red_main = PIDNavigatorRed()
    pid_navigator_red_main.navigate()
