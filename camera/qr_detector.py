import cv2

# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)

    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        if data:
            print("data found: ", data)
    if(cv2.waitKey(1) == ord("q")):
        print("quitting!")
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()


