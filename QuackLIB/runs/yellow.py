"""
This is the yellow run, it's the first run out of 5 runs.
in this run our robot doe's TO BE CONTENU!!!
"""
#!/usr/bin/env pybricks-micropython

#imports 
from QuackLIB.funcs import straight_gyro
from QuackLIB.funcs import gyro
from QuackLIB.funcs import pid_line_follower
from QuackLIB.funcs import turn_to


def bridge():
    # Going to the black line and following it until we get to the bridge
    straight_gyro(80, 90, gyro.angle())
    turn_to(45)
    straight_gyro(150, 300, gyro.angle())
    pid_line_follower(100, 600)

    straight_gyro(120, 200, gyro.angle()) # Starting to go with gyro to put the truck in it's place

    # Going forwards and then backwards to drop the 2 parts of the bridge using the lego band
    straight_gyro(125, 120, gyro.angle())
    straight_gyro(-110, -132.5, gyro.angle())

def cargo_connect_circle():
    # Going towards the cube's dropoff and turning to leave the cube there
    straight_gyro(110, 195, gyro.angle())
    turn_to(175)

    # Getting away from the dropoff
    straight_gyro(200, 10, 90)
    straight_gyro(-120, -70, 175)
    
def train_truck():
    # Turning to the truck
    turn_to(135)

    # Going to the truck
    straight_gyro(110, 325, gyro.angle())
    turn_to(95)

    # putting down the truck
    straight_gyro(105, 150, 95)
    straight_gyro(-100, -66, 100)

    # turning to the helicopter
    turn_to(-5)
    straight_gyro(120, 397, 0)
    turn_to(88)

def helicopter_drop_package():
    # Pushing the helicopter's handle and dropping the package
    straight_gyro(110, 230, 87)
    straight_gyro(-110, -120, gyro.angle())
    turn_to(180)

def going_home_and_container():
    # going back home
    straight_gyro(100, 40, gyro.angle())
    turn_to(250)
    straight_gyro(300, 760, 262)
    turn_to(220)
    straight_gyro(150, 210, gyro.angle())
    turn_to(270)

    # taking blue container
    straight_gyro(1000, 759, 292)



def main_yellow():
    # reseting the gyro
    gyro.reset_angle(0)

    # missions by order
    bridge()
    cargo_connect_circle()
    train_truck()
    helicopter_drop_package()
    going_home_and_container()