#!/bin/env python3

from motors import motors
from colorsensor import colo
from distanceSensor import rpTut
from explorerhat import touch as button
from explorerhat import motor
import time
from navigation_leander_w_history import PIDNavigatorRed


class SimpleNavigatorRed:

    def navigation(self, color_sensor):
        while True:
            if button.four.is_pressed():
                motor.stop()
                break
            while rpTut.distance() < 10: #avoid collisions
                motor.stop()
            if color_sensor.get_color()[0] < 80:                    
                motor.one.forward(100)          
            if color_sensor.get_color(True, False)[0] > 50: 
                motor.two.forward(100)
            time.sleep(0.02)
            # motor.stop()

if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    simple_navigator_red = SimpleNavigatorRed()
    pid_navigator_red = PIDNavigatorRed()
    slow_pid_navigator_red = PIDNavigatorRed(True)
    while True:
        if button.one.is_pressed():
            simple_navigator_red.navigation(color_sensor)
        if button.two.is_pressed():
            pid_navigator_red.navigation(color_sensor)
        if button.three.is_pressed():
            slow_pid_navigator_red.navigation(color_sensor)

