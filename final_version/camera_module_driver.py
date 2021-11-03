import cv2

class CameraModuleDriver:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()

    def __del__(self):
        self.cap.release()

    def scan_qr_code(self):
        _, img = self.cap.read()
        data, bbox, _ = self.detector.detectAndDecode(img)
        if bbox is not None:
            if data:
                return data
        else:
            return None

