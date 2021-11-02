from collision_avoidance import CollisionAvoidance
from color_sensor_driver import ColorSensorDriver
from explorerhat import motor
import simple_pid
import time


class LineFollowing:
    def __init__(self, ebd):
        self.color_sensor_driver = ColorSensorDriver()
        self.collision_avoidance = CollisionAvoidance(ebd)
        self.emergency_break_driver = ebd
        self.limit = 30
        self.pid_controller = simple_pid.PID(5, 1, 0.01, setpoint=20,
                                             output_limits=(-self.limit, self.limit))

    def follow_line(self):
        while self.collision_avoidance.avoid_collision():    # and check for emergency break
            if self.emergency_break_driver.emergency_break_detected:
                break
            control = self.pid_controller(self.color_sensor_driver.get_color()[0])
            print("control: ", control)
            motor.one.forward(70 - control)  # left motor
            motor.two.forward(70 + control)  # right motor
            time.sleep(0.02)
            if self.color_sensor_driver.get_color()[0] <= 16 or \
                    self.color_sensor_driver.get_color()[0] > 70:
                motor.backward(100)
                time.sleep(0.01)
            motor.stop()
