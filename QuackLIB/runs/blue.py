"""
This is the blue run. it's the 4 run out of 5, in this run the robot starts moving forward and
tracking the black line, from there the robot flips the engine, goes backwards, and leaves the green container
on the container color matching area. from this run we get 60pts.
"""

#!/usr/bin/env pybricks-micropython

# imports
from library import straight_gyro
from library import pid_line_follower
from library import gyro


def main_blue():
    gyro.reset_angle(0) # Starts with resetting the gyro's value
    
    # Goes towards the engine
    straight_gyro(170, 290, 0)
    pid_line_follower(150, 550)

    straight_gyro(150, 50, 48) # Flipping the engine

    # Going back home
    straight_gyro(-200, -200, 45)
    straight_gyro(-12300, -700, 45)
    
 
 
    