import board
import adafruit_tcs34725


class ColorSensorDriver:
    def __init__(self):
        self.i2c = board.I2C()
        self.sensor = adafruit_tcs34725.TCS34725(self.i2c)
        self.color = self.sensor.color_rgb_bytes

    def get_color(self, new_colors_from_sensor=True):
        if new_colors_from_sensor:
            self.color = self.sensor.color_rgb_bytes
        return self.color


# Testing
if __name__ == '__main__':
    color_sensor_driver = ColorSensorDriver()
    while True:
        print(color_sensor_driver.get_color())
