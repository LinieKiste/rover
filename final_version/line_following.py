#!/bin/python3
from collision_avoidance import CollisionAvoidance
from color_sensor_driver import ColorSensorDriver
from explorerhat import motor
import simple_pid
import time


class LineFollowing:
    def __init__(self, ebd):
        self.color_sensor_driver = ColorSensorDriver()
        self.collision_avoidance = CollisionAvoidance(ebd)
        self.emergency_break_driver = ebd
        self.limit = 20
        self.pid_controller = simple_pid.PID(5, 1, 0.01, setpoint=17,
                                             output_limits=(-self.limit, self.limit))

    def follow_line(self, move_fast=False):
        if move_fast:
            self.pid_controller.setpoint = 30
        else:
            self.pid_controller.setpoint = 17
        while not self.collision_avoidance.avoid_collision():    # and check for emergency break
            control = self.pid_controller(self.color_sensor_driver.get_color()[0])
            print("control: ", control)
            print("color: ", self.color_sensor_driver.get_color()[0])
            motor.one.forward(60 - control)  # left motor
            motor.two.forward(60 + control)  # right motor
            if move_fast:
                time.sleep(0.02)
                if self.color_sensor_driver.get_color()[0] <= 16 or \
                    self.color_sensor_driver.get_color()[0] > 60:
                    motor.backward(100)
                    time.sleep(0.03)
            else:
                if self.color_sensor_driver.get_color()[0] != 17:
                    motor.backward(100)
                    time.sleep(0.006)
            motor.stop()
            time.sleep(0.01)
