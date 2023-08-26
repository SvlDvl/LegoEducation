from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

# Create objects here.

hub = MSHub()
color_sensor = ColorSensor('D')
motors = MotorPair('E','A')

timer = Timer()

count = 0

while timer.now() < 60:
    color = color_sensor.wait_for_new_color()
    if color == 'yellow':
        count = count + 1
        hub.light_matrix.write(count)
        motors.move(2,'seconds')
        print(count)