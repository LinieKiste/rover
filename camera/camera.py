from picamera import PiCamera
import time
from explorerhat import motor
import cv2

class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        self.rot = 80

    def __del__(self):
        self.cap.release()

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

    def rotate(self, left):
        x = self.rot
        if left:
            motor.one.forward(x)
            motor.two.backward(x)
        else:
            motor.one.backward(x)
            motor.two.forward(x)

    def find(self):
        for i in range(20):
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
                return data
                break
            else:
                self.rotate(True)
                time.sleep(.1)
        
if __name__ == '__main__':
    c = Camera()
    c.find()
    while False:
        res = c.scan_qr_code()
        if res is not None:
            print(f"data: {res}")

