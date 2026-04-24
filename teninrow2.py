#!/usr/bin/env pybricks-micropython
# Import necessary libraries
from pybricks.ev3devices import ColorSensor, Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# ---------- STANDARD SETUP CODE ---------- #

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialise the sensors.
light_sensor = ColorSensor(Port.S3)
distance_sensor = UltrasonicSensor(Port.S4)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)

# ---------- MAINLINE PROGRAM ---------- #

### Here is where your code starts ###

adjust = 1.2
threshold = 40
speed = 80
turn_rate = 1.3


def drive(speed, rotation, distance):
    robot.drive(speed, rotation)
    wait(distance)
    robot.stop()


while True:
    colour = light_sensor.rgb()
    r, g, b = colour
    reflection = round((r + g + b) / 3)
    turn = (reflection - threshold) * turn_rate
    if reflection > 28:
        colour = light_sensor.rgb()
        r, g, b = colour
        reflection = round((r + g + b) / 3)
        turn = (reflection - threshold) * turn_rate
        robot.drive(speed - abs(turn * adjust), turn)
        print(reflection)
    else:
        if str(light_sensor.color()) == "Color.BLACK":
            drive(100, -90, 400)
            break
        drive(100, -90, 400)

while True:
    colour = light_sensor.rgb()
    r, g, b = colour
    reflection = round((r + g + b) / 3)
    turn = reflection - threshold
    dist = distance_sensor.distance()
    if dist < 140:
        robot.stop()
        drive(80, 35, 1500)
        drive(80, -25, 4500)
    if g > (r + b) / 1.2:  # green
        drive(50, 0, 200)
        drive(50, -85, 300)
    if r > (g + b) / 1.2:  # red
        drive(50, 0, 800)
        drive(50, 85, 300)
    robot.drive(speed - abs(turn * adjust), turn)
    print(turn)
