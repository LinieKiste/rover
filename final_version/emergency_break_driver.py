#!/bin/python3
from RPi import GPIO
from explorerhat import motor


class EmergencyBreakDriver:
    def __init__(self):
        self.emergency_break_detected = False

    def emergency_break_check(self):
        if not self.emergency_break_detected and GPIO.input(22) == 1:
            motor.stop()
            self.emergency_break_detected = True
            print("emergency break detected")
        return self.emergency_break_detected
