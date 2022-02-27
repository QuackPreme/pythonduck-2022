#!/usr/bin/env pybricks-micropython

# imports #
from pybricks.hubs import EV3Brick as ev3b
from pybricks.parameters import Button

from QuackLIB.runs.yellow import main_yellow as yellow_run
from QuackLIB.runs.white import main_white as white_run
from QuackLIB.runs.green import main_green as green_run
from QuackLIB.runs.blue import main_blue as blue_run
from QuackLIB.runs.red import main_red as red_run

# start special count variable
count_click = 0

#defining the main with the buttons
def get_input():
    # global variables #
    global count_click
    # List of the buttons that are pressed #
    button_pressed = ev3b.buttons.pressed()

    # The ifs to check what to run #
    if button_pressed != None: # if button_pressed is not empty
        # if the center button is pressed
        if Button.CENTER in button_pressed: 
            # Adding to the click count 1 everytime the center button is clicked
            count_click += 1

            # The ifs to checkwhich run to run by click number
            if count_click == 1: # yellow run
                print("Yellow")
                yellow_run()

            elif count_click == 2: # white run
                print("White")
                white_run()

            elif count_click == 3: # green run
                print("green")
                green_run()

            elif count_click == 4: # blue run
                print("Blue")
                blue_run()

            elif count_click == 5: # red run
                print("Red")
                red_run()


        # if the top button is pressed - white run
        elif Button.UP in button_pressed:
            print("White")
            white_run()

        # if the bottom button is pressed - blue run
        elif Button.DOWN in button_pressed:
            print("Blue")
            blue_run()

        # if the right button is pressed - green run
        elif Button.RIGHT in button_pressed:
            print("Green")
            green_run()

        # if the left button is pressed - red run
        elif Button.LEFT in button_pressed:
            print("Red")
            red_run()

# statement to run the main file
if __name__ == '__main__':
    count_click = 0
    while True:
        get_input()