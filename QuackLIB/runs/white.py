"""
This is the white run. It goes to the blue door without moving the chicken statue,
placing on it the yellow package and going back hom.
"""

#!/usr/bin/env pybricks-micropython
from QuackLIB.funcs import straight_gyro, turn_to, gyro

def going_to_the_door():
    straight_gyro(200, 1100, 0)
    straight_gyro(110, 200, 55)
    turn_to(0)

def droping_the_package():
    straight_gyro(170, 170, 10)

def home():
    straight_gyro(-120, -117.5, 0)
    straight_gyro(-120, -200, 55)
    turn_to(180)
    straight_gyro(1000, 1310, 180)


def main_white():
    # reseting the gyro
    gyro.reset_angle(0)

    # missions by order
    going_to_the_door()
    droping_the_package()
    home()