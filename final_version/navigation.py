from emergency_break_driver import EmergencyBreakDriver
from explorerhat import touch as button
from line_following import LineFollowing
from location_finding import LocationFinding


def navigation():
    emergency_break_driver = EmergencyBreakDriver()
    line_following = LineFollowing(emergency_break_driver)
    location_finding = LocationFinding(emergency_break_driver)
    while True:
        emergency_break_driver.emergency_break_detected = False
        if button.one.is_pressed():
            print("You pressed button 1: line following")
            line_following.follow_line()
        elif button.two.is_pressed():
            print("You pressed button 2: location finding")
            location_finding.find_location()
        elif button.four.is_pressed():
            break
