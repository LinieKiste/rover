from picamera import PiCamera
from time import sleep
import cv2

class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()

    def __del__(self):
        self.cap

    # returns either None or the data and the bounding size and distance from the center
    # pretty sure the size thing is wrong and the distance also but not as sure as with the size
    def scan_qr_code(self):
        _, img = self.cap.read()
        data, bbox, _ = self.detector.detectAndDecode(img)

        if bbox is not None:
            if data:
                return data
        else:
            return None
        
if __name__ == '__main__':
    c = Camera()
    while True:
        res = c.scan_qr_code()
        if res is not None:
            print(f"data: {res}")

