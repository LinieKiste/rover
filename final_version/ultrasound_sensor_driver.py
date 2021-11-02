# !/bin/python3
from RPi import GPIO
import time


class UltrasoundSensorDriver:
    def __init__(self):
        # GPIO Mode (BOARD or BCM)
        GPIO.setmode(GPIO.BCM)
        # set GPIO Pins
        self.GPIO_TRIGGER = 6
        self.GPIO_ECHO = 24
        # set GPIO direction (IN or OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance_to_object(self):
        # set Trigger to HIGH and back to LOW after 0.01ms
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
        # start measurement
        while GPIO.input(self.GPIO_ECHO) == 0:
            pass
        start_time = time.time()
        while GPIO.input(self.GPIO_ECHO) == 1:
            pass
        stop_time = time.time()
        return stop_time - start_time
