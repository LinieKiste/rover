#!/bin/python3
from collision_avoidance import CollisionAvoidance
from explorerhat import motor
import time
import cv2


class LocationFinding:
    def __init__(self, ebd):
        self.collision_avoidance = CollisionAvoidance(ebd)
        self.emergency_break_driver = ebd

        self.cap = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        self.rot = 80

    def __del__(self):
        self.cap.release()

    # just call this function
    def find_location(self):
        while not self.emergency_break_driver.emergency_break_check():
            first_rot = False
            while not self.emergency_break_driver.emergency_break_check():
                motor.stop()
                start = time.time()
                timer = 0
                data = None
                while timer < .7:
                    try:
                        data = self.scan_qr_code()
                    except:
                        print("error, exiting manually...")
                        exit()
                    if data is not None:
                        # instructions(data + '.txt')
                        break
                    timer = time.time() - start
    
                if data is not None:
                    # return data
                    break
                else:
                    self.rotate(True)
                    time.sleep(.05)
                    first_rot = True

            if data is not None:
                print(f"found QR code data: {data}")
                if first_rot :
                    self.rotate(True) # Turn back a little to center back onto the code
                    time.sleep(.035)
                motor.forward(60)
                while not self.collision_avoidance.check_for_collison():
                    pass
                motor.stop()

    def scan_qr_code(self):
        _, img = self.cap.read()
        data, bbox, _ = self.detector.detectAndDecode(img)

        if bbox is not None:
            if data:
                return data
        else:
            return None

    def rotate(self, left):
        x = self.rot
        if left:
            motor.one.forward(x)
            motor.two.backward(x)
        else:
            motor.one.backward(x)
            motor.two.forward(x)

if __name__ == '__main__':
    from emergency_break_driver import EmergencyBreakDriver
    l = LocationFinding(EmergencyBreakDriver())
    l.find_location()

