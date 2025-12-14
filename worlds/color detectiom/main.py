#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()

color_sensor_in1 = ColorSensor(INPUT_1)
ultrasonic_sensor_in2 = UltrasonicSensor(INPUT_2)
gyro_sensor_in3 = GyroSensor(INPUT_3)
gps_sensor_in4 = GPSSensor(INPUT_4)
pen_in5 = Pen(INPUT_5)

motorC = LargeMotor(OUTPUT_C) # Magnet

# Here is where your code starts

color = None
target = None
color_found = None
outside = None
inside = None

# Describe this function...
def do_something():
    global color, target, color_found, outside, inside
    color = color_sensor_in1.reflected_light_intensity - 50
    outside = 1 - color
    inside = 10 + color
    tank_drive.on(outside, inside)


tank_drive.on(20, 20)
color_found = 'Null'
while True:
    if color_found != color_sensor_in1.color_name:
        color_found = color_sensor_in1.color_name
        print(color_found)
        if color_found == 'Black':
            tank_drive.off(brake=True)
            break
