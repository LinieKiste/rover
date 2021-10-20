from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.capture('/home/pi/rover/camera/image.jpg')


