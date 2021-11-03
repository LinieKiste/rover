#!/bin/python3
from emergency_break_driver import EmergencyBreakDriver
from explorerhat import touch as button
from explorerhat import light
from line_following import LineFollowing
from location_finding import LocationFinding

def navigation():
    emergency_break_driver = EmergencyBreakDriver()
    line_following = LineFollowing(emergency_break_driver)
    location_finding = LocationFinding(emergency_break_driver)
    while True:
        light.on()
        emergency_break_driver.emergency_break_detected = False
        if button.one.is_pressed():
            light.off()
            light.blue.on()
            print("You pressed button 1: slow line following")
            line_following.follow_line()
        elif button.two.is_pressed():
            light.off()
            light.yellow.on()
            print("You pressed button 2: fast line following")
            line_following.follow_line(True)
        elif button.three.is_pressed():
            light.off()
            light.red.on()
            print("You pressed button 3: location finding")
            location_finding.find_location()
        elif button.four.is_pressed():
            light.off()
            light.green.on()
            break


if __name__ == "__main__":
    navigation()

