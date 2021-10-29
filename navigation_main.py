#!/bin/env python3

# from motors import motors
from colorsensor import colo
# from distanceSensor import rpTut
from explorerhat import touch as button
from explorerhat import motor
# from RPi import GPIO
import time
from navigation_leander_w_history import PIDNavigatorRed, CollisionAndEmergencyBreakHandler, PIDNavigatorRedSimple, PIDNavigatorRedSlow
from navigation_tommaso import SimpleNavigatorRed


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    caebh = CollisionAndEmergencyBreakHandler()
    simple_navigator_red = SimpleNavigatorRed(caebh)
    pid_navigator_red = PIDNavigatorRedSlow(color_sensor1, caebh)
    pid_navigator_red_simple = PIDNavigatorRedSimple(color_sensor1, caebh)
    while True:
        if button.one.is_pressed():
            time.sleep(0.1)
            print("B1 pressed: SimpleNavigatorRed")
            print("Press button 1 if the rover will drive clockwise\nPress button 2 if the rover will  drive counterclockwise")
            while True:
                if button.one.is_pressed():
                    print("Rover driving clockwise")
                    simple_navigator_red.navigate(color_sensor1, True)
                    break
                elif button.two.is_pressed():
                    print("Rover driving counterclockwise")
                    simple_navigator_red.navigate(color_sensor1, False)
                    break
                elif caebh.check_for_emergency_break():
                    break

        elif button.two.is_pressed():
            print("B2 pressed: PIDNavigatorRed")
            pid_navigator_red.navigate()
        elif button.three.is_pressed():
            print("B3 pressed: PIDNavigatorRedSimple")
            pid_navigator_red_simple.navigate()

