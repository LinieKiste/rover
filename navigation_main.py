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
from camera.camera import Camera


if __name__ == "__main__":
    color_sensor1 = colo.ColorSensor()
    # cam = Camera()
    caebh = CollisionAndEmergencyBreakHandler()
    simple_navigator_red = SimpleNavigatorRed(caebh)
    pid_navigator_red = PIDNavigatorRedSlow(color_sensor1, caebh)
    pid_navigator_red_simple = PIDNavigatorRedSimple(color_sensor1, caebh)
    pid_navigator_red_final = PIDNavigatorRed(color_sensor1, caebh) 
    # QR CODE STUFF
    #qr_data = cam.find()
    #motor.stop()
    #if qr_data is not None:
    #    print(f"found qr code data: {qr_data}")
    #    cam.rotate(False)
    #    time.sleep(.1)
    #    motor.forward(60)
    #    while True:
    #        if caebh.check_for_collision():
    #            motor.stop()
    #            exit()
    print("No QR-code found, continuing with line-following behavior")
    while True:
        if button.one.is_pressed():
            time.sleep(0.25)
            print("B1 pressed: SimpleNavigatorRed")
            print("Press button 1 if the rover will drive clockwise\nPress button 2 if the rover will drive counterclockwise")
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
            print("B2 pressed: PIDNavigatorRedSlow")
            pid_navigator_red.navigate()
        elif button.three.is_pressed():
            print("B3 pressed: PIDNavigatorRedSimple")
            pid_navigator_red_simple.navigate()
        elif button.four.is_pressed():
            print("B4 pressed: PIDNavigatorRed")
            pid_navigator_red_final.navigate()
