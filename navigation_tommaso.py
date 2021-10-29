#!/bin/env python3

# from motors import motors
from colorsensor import colo
# from distanceSensor import rpTut
from explorerhat import touch as button
from explorerhat import motor
# from RPi import GPIO
import time
from navigation_leander_w_history import CollisionAndEmergencyBreakHandler


class SimpleNavigatorRed:
    def __init__(self, collision_and_emergency_break_handler):
        self.caebh = collision_and_emergency_break_handler

    def navigate(self, color_sensor, clockwise):
        while True:
            if self.caebh.check_for_collision_and_emergency_break():
                break
            if color_sensor.get_color()[0] > 70:
                if clockwise == False:
                    motor.one.forward(100)
                else:
                    motor.two.forward(100)
            if color_sensor.get_color()[0] < 50:
                if clockwise == False:
                    motor.two.forward(100)
                else:
                    motor.one.forward(100)
            else:
                motor.forward(100)
            time.sleep(0.025)
            motor.stop()

if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    caebh = CollisionAndEmergencyBreakHandler()
    simple_navigator_red = SimpleNavigatorRed(caebh)
    simple_navigator_red.navigate(color_sensor1)
