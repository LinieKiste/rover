#!/bin/python3
from ultrasound_sensor_driver import UltrasoundSensorDriver
from explorerhat import motor
import time


class CollisionAvoidance:
    def __init__(self, ebd):
        self.distance_sensor_driver = UltrasoundSensorDriver()
        self.emergency_break_driver = ebd

    def avoid_collision(self):
        while not self.emergency_break_driver.emergency_break_check():
            # No object closer than 15 cm if sound needs more than 0.001 s to come back
            # (sonic speed: 34 300 000 m/s)
            if self.distance_sensor_driver.distance_to_object() > 0.001:
                break
            else:
                motor.stop()


# Testing
from emergency_break_driver import EmergencyBreakDriver

if __name__ == '__main__':
    collision_handler = CollisionAvoidance(EmergencyBreakDriver())
    while True:
        motor.forward(100)
        collision_handler.avoid_collision()
        time.sleep(0.02)
        motor.stop()
