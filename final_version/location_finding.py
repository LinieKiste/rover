#!/bin/python3
from collision_avoidance import CollisionAvoidance
from explorerhat import motor
from camera_module_driver import CameraModuleDriver
import time

class LocationFinding:
    def __init__(self, ebd):
        self.collision_avoidance = CollisionAvoidance(ebd)
        self.emergency_break_driver = ebd
        self.camMod = CameraModuleDriver()

    def find_location(self):
        while not self.emergency_break_driver.emergency_break_check():
            data = self.camMod.scan_qr_code()
            for _ in range(8):
                if data is None:
                    data = self.camMod.scan_qr_code()
            motor.one.forward(100)
            motor.two.backward(100)
            time.sleep(.03)

            if data is not None:
                print(f"found QR code data: {data}")
                motor.forward(70)
                while not self.collision_avoidance.check_for_collison():
                    pass
            motor.stop()

if __name__ == '__main__':
    from emergency_break_driver import EmergencyBreakDriver
    l = LocationFinding(EmergencyBreakDriver())
    l.find_location()

