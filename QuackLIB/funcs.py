# imports #
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor, LiftMotor)
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
import time
from sys import exit
import math
# Brick instance
ev3 = EV3Brick()

# Motor Variables #
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
LiftMotor = Motor(Port.A)
# Chassis var #
robot = DriveBase(left_motor, right_motor, wheel_diameter=53, axle_track=90)

# Sensors
gyro = GyroSensor(Port.S1)
color_sensor = ColorSensor(Port.S2)

# Wheel Diameter #
wheel_distance = 20
wheel_diameter = 53
WHEEL_CIRCUMFERENCE = 6

# Moving straight (backward / forward) using the gyro sensor. Receiving distance as a parameter.
def straight_gyro(speed=100, distance=1000, starting_angle=0):
    offset = starting_angle # Starting angle - the angle we always fix to.
    
    # P.I.D variables
    kp = 2.9
    ki = 0.01
    kd =0.01
    
    integral = 0
    last_error = 0
    
    # Essential robot variables 
    start_point = robot.distance()
    compareVal = distance / abs(distance)
    
    # Cals #
    robot_distance_cal = (robot.distance() - start_point) * int(compareVal)
    compare_cal = distance * int(compareVal)

    # While the robot distance cal is smaller than the comapre cal
    while  robot_distance_cal < compare_cal: # handling erros
        error = gyro.angle() - offset
        
        # Defining what we need to calculate the correction (integral & drivative & last_error)
        integral += error
        derivative = error - last_error
        last_error = error
        correction = (error * kp) + (integral * ki) + (derivative * kd) # Setting up the correction using all the P.I.D variables we set earlier in the code

        robot.drive(speed, -correction) # Initiating the drive using the preset speed & correction
        
        last_error = error # Redefining last_error to keep the correction changing at all times

    robot.stop() # Stop driving and end the function

    
# Turning using the gyro sensor. Also gets the intended spin angle as a parameter.
def turn_to(target_angle):
    kp = 2
    speed = 3
    while abs(speed) > 1:
        error = target_angle - gyro.angle()
        speed = max(-100, min(100, error)) * 4

        # this part determines the minimal speed >>
        if abs(speed) < 3  and speed != 0: 
            speed = 5 * abs(speed) / speed
        
        tank_drive_on(speed, -speed)

    tank_drive_off()
    exit


# Following a black line using the color sensor and a P.I.D code (the color of the line followed can be changed).
def pid_line_follower(speed = 200, distance = 500):
    # Def P.I.D variabals
    target = 25
    kp = 0.9003
    ki = 0.000001
    kd = 0.7005
    last_error = 0
    integral = 0
    start = robot.distance() # start distance
    while robot.distance() - start < distance:
        value = color_sensor.reflection()
        error = target - value 
        integral += error
        derivative = error - last_error
        correction = (error * kp) + (integral * ki) + (derivative * kd) 
        robot.drive(speed, correction * -1)
        last_error = error
    robot.stop()


# Just a simple code designed for cleaning the robot's wheels.
def cleaning():
    while True:
        robot.drive(80, 0)

# Drives forward until seeing a certain color and uses the color sensor (gets the target color as a parameter).
def straight_gyro_to_color(target_reflection, speed=200):
    kp = 2.5
    while color_sensor.reflection() != target_reflection:
        error = gyro.angle()
        robot.drive(speed, -error * kp)
    print(gyro.angle())
    robot.stop()    

def tank_drive_on(left_speed, right_speed): # turns tank drive on with these specified speeds, does not turn off
    left_motor.run(left_speed)
    right_motor.run(right_speed)

def tank_drive_off(): # turns tank drive off
    left_motor.stop()
    right_motor.stop()

def tank_drive_break(): # breaks
    left_motor.hold()
    right_motor.hold()

def tank_drive_time(left_speed, right_speed, period): # driving by time
    tank_drive_on(left_speed, right_speed)
    time.sleep(period)
    tank_drive_break()

def arch_drive(distance, target_angle):
    # variables
    DISTANCE_KP = 0.0
    DISTANCE_KI = 0.0
    
    DEFULT_SPEED = 100
    
    ANGLE_KP = 0.0
    ANGLE_KI = 0.0
    
    speed_high = 1
    
    distance_integral = 0
    angle_integral = 0
    
    # calculates the circle
    angle = target_angle - gyro.angle
    circumference = (distance / angle) * 360
    
    # calculates the speed ratio
    radius = circumference / (2 * 3.1415926)
    ratio_radius_to_wd = radius / wheel_distance
    ratio_low_to_high = (1 / (ratio_radius_to_wd))
    ratio_low_to_high = -(ratio_low_to_high - speed_high)
    
    
    # calculates which wheel needs to drive more 
    if (angle < 0):
        high_motor = right_motor
        low_motor = left_motor
    else:
        high_motor = left_motor
        low_motor = right_motor
    
    # the offset
    distance_offset = high_motor.position * WHEEL_CIRCUMFERENCE
    # move
    while (high_motor.position * WHEEL_CIRCUMFERENCE - distance_offset != distance and gyro.angle != target_angle):
        # calculates the distance
        distance_centimeters = high_motor.position * WHEEL_CIRCUMFERENCE
        
        # calculates the errors
        error_distance = distance - (distance_centimeters - distance_offset)
        error_angle = (((distance_centimeters - distance_offset) / circumference) * 360) - gyro.angle
            
        # adds the error to the integral
        distance_integral += error_distance
        angle_integral += error_angle
        
        # calculates the speeds based on the errors
        speed_high = DEFULT_SPEED + error_distance * DISTANCE_KP + distance_integral * DISTANCE_KI
        speed_lower = speed_high * ratio_low_to_high + error_angle * ANGLE_KP + angle_integral * ANGLE_KI
        
        
        # drives
        high_motor.on(min(max(speed_high, -100), 100))
        low_motor.on(min(max(speed_lower, -100), 100))
        
    # stops
    high_motor.off()
    low_motor.off()

    
