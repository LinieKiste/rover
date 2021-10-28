#!/bin/env python3

# from motors import motors
from colorsensor import colo
# from distanceSensor import rpTut
from explorerhat import touch as button
from explorerhat import motor
# from RPi import GPIO
import time
from navigation_leander_w_history import PIDNavigatorRed, CollisionAndEmergencyBreakHandler


class SimpleNavigatorRed:
    def __init__(self, collision_and_emergency_break_handler):
        self.caebh = collision_and_emergency_break_handler

    def navigate(self, color_sensor):
        while True:
            if self.caebh.check_for_collision_and_emergency_break():
                break
            if color_sensor.get_color()[0] < 80:                    
                motor.one.forward(100)          
            if color_sensor.get_color(True, False)[0] > 50: 
                motor.two.forward(100)
            time.sleep(0.02)
            motor.stop()

if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    caebh = CollisionAndEmergencyBreakHandler()
    simple_navigator_red = SimpleNavigatorRed(caebh)
    pid_navigator_red = PIDNavigatorRed(color_sensor1, caebh)
    pid_navigator_red_simple = PIDNavigatorRedSimple(color_sensor1, caebh)
    while True:
        if button.one.is_pressed():
            simple_navigator_red.navigate(color_sensor1)
        if button.two.is_pressed():
            pid_navigator_red.navigate()
        if button.three.is_pressed():
            pid_navigator_red_simple.navigate()

