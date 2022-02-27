"""
This is the green run. it's the 3 run out of 5, this run is the most short and fast run
all this run does is going forward and backwards, but by doing that the robot puts the big delivery on the blue platform
partly, and makes 20pts.
"""
#!/usr/bin/env pybricks-micropython
from QuackLIB.funcs import straight_gyro, gyro


def main_green():
    # reset the gyros value to 0 in the start of the run
    gyro.reset_angle(0)

    # Going straight to put the container in the circle and the wing on the stand
    straight_gyro(200, 485, 0)
    straight_gyro(100, 165, 0)

    straight_gyro(-2000, -650, 0) # Going back home
