"""
this is the red run, it's the last run out of 5 runs.
in this run we start by folowing the black line, then
we stop that and start going to the crane. we
do the crane with an arm that conected to the robot, the robot go's
backwords. when he go's back is arm poshing the crane.
then the robot go's forwords to the accident prevention misson, 
he do that with is tiny arm and is blocker 

"""


#!/usr/bin/env pybricks-micropython
from QuackLIB.funcs import straight_gyro, tank_drive_time, gyro, pid_line_follower, turn_to

def getting_near_missions():
    # Going to the black line and following it until we get near the bridge
    straight_gyro(80, 80, 0)
    turn_to(45)
    straight_gyro(150, 300, 45)
    pid_line_follower(120, 640)


def crane():
    # Going towards the crane in a 45 degree drive
    straight_gyro(120, 240, 45)
    turn_to(-85)

    straight_gyro(-90, -375, -85) # Going backwards to finish the crane


def accident_prevention():
    # Going towards the final mission 
    straight_gyro(150, 400, -85)
    straight_gyro(100, 220, -50)
    turn_to(-85)
    
    # Dropping the yellow part of the mission and staying there
    straight_gyro(100, 1, -85)
    tank_drive_time(125, 125, 5)
    print("Good avoda!")


def main_red():
    gyro.reset_angle(0) # Starts with resetting the gyro's value

    # Starting to do the missions
    getting_near_missions()
    crane()
    accident_prevention()

    