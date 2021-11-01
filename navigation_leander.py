#!/bin/env python3

from colorsensor import colo
from distanceSensor import rpTut
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


class PIDNavigatorRed:
    def __init__(self):
        self.caebh = CollisionAndEmergencyBreakHandler()
        self.color_sensor = colo.ColorSensor()
        self.limit_pid_slow = 24
        self.setpoint_pid_slow = 40
        self.pid_controller_pid_slow = \
            simple_pid.PID(5, 1, 0.01, setpoint=self.setpoint_pid_slow,
                           output_limits=(-self.limit_pid_slow, self.limit_pid_slow))
        self.base_speed_pid_fast = 41
        self.limit_pid_fast = 10
        self.motors_status_pid_fast = {motor.one: False, motor.two: False}
        self.pid_controller_pid_fast = \
            simple_pid.PID(1, 10, 0, setpoint=50,
                           output_limits=(-self.limit_pid_fast, self.limit_pid_fast))

    def navigate(self):
        # move the rover to the right side of the line
        # motor.two.backward(100)
        # time.sleep(0.3)
        # motor.forward(100)
        # time.sleep(0.15)
        motor.stop()
        while True:
            self.motors_status_pid_fast = {motor.one: False, motor.two: False}
            if self.navigate_fast():
                motor.backward(100)
                time.sleep(0.1)
                if self.navigate_slowly():
                    pass
                else:
                    break
            else:
                break
            motor.backward(100)

    def navigate_slowly(self):
        print("entered slow navigating")
        perfect_color_detected = 0
        while not self.caebh.check_for_collision_and_emergency_break():
            motor.stop()
            if self.setpoint_pid_slow -20 < self.color_sensor.get_color()[0] < 20 + self.setpoint_pid_slow:
                perfect_color_detected += 1
            if perfect_color_detected > 10:
                return True
            elif self.color_sensor.get_color()[0] <= 16 or \
                    self.color_sensor.get_color()[0] > 70:
                motor.backward(100)
                perfect_color_detected = 0
            control = self.pid_controller_pid_slow(self.color_sensor.get_color()[0])
            print("control: ", control)
            motor.one.forward(66 - control)  # left motor
            motor.two.forward(66 + control)  # right motor
            time.sleep(0.03)
        return False

    def kickstart(self, motors_list):
        for m in motors_list:
            m.forward(100)
            self.motors_status_pid_fast[m] = True
        time.sleep(0.02)

    def forward(self, motors_list, speed):
        for m in motors_list:
            if speed == 0:
                self.motors_status_pid_fast[m] = False
            elif not self.motors_status_pid_fast[m]:
                self.kickstart([m])
            m.forward(speed)

    def navigate_fast(self):
        print("entered fast navigating")
        while not self.caebh.check_for_collision_and_emergency_break(self):
            if 100 < self.color_sensor.get_color()[0] <= 16:
                return True
            control = self.pid_controller_pid_fast(self.color_sensor.get_color()[0])
            print("control: ", control)
            # left motor
            # if control == self.limit_pid_fast:
                # self.forward([motor.one], 0)
            # else:
            self.forward([motor.one], self.base_speed_pid_fast - control)
            # right motor
            # if control == -self.limit_pid_fast:
                # self.forward([motor.two], 0)
            # else:
            self.forward([motor.two], self.base_speed_pid_fast + control)
        return False


if __name__ == "__main__":
    pid_navigator_red_main = PIDNavigatorRed()
    pid_navigator_red_main.navigate()
