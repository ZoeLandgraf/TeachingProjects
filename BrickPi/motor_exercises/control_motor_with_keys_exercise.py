# This code is largely adapted from: https://github.com/DexterInd/BrickPi/blob/master/Software/BrickPi_Python/

from __future__ import print_function
from __future__ import division
from builtins import input

import time

# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print(),
# the integer division and input()
# mind your parentheses!

import sys
sys.path.append("/home/zoe/Teaching/")

import brickpi3 as bp
#from Tutoring.BrickPi3.Software.Python import brickpi3 as bp

BP = bp.BrickPi3()

right_motor_power = 20
left_motor_power = 20
right_motor = BP.PORT_D
left_motor = BP.PORT_A

try:
    while True:

        a = input()

        if a == "Go" or a == "gO" or a == "go" or a == "GO" or a == "g" or a == "G":
            BP.set_motor_power(right_motor, right_motor_power)
            BP.set_motor_power(left_motor, left_motor_power)
            print("Moving forward at speed ", right_motor_power)
            a = "I" #i for idle, don't do anything but wait for next input

        elif a == "Stop" or a == "stop" or a == "STOP" or a == "s" or a == "S":
            BP.set_motor_power(right_motor, 0)
            BP.set_motor_power(left_motor, 0)
            print("Stopped")
            a = "I"  # i for idle, don't do anything but wait for next input
	elif a == "left" or a == "Left" or a == "LEFT" or a == "l" or a == "L":
	    #the firt two lines stop the motors and the second two get the robot to start turning
	    BP.set_motor_power(right_motor, 0)
            BP.set_motor_power(left_motor, 0)
	    BP.set_motor_power(right_motor, right_motor_power)
	    BP.set_motor_power(left_motor, -left_motor_power)
	    print("Currently turning left")
	elif a == "right" or a == "Right" or a == "RIGHT" or a == "r" or a == "R":
            BP.set_motor_power(right_motor, 0)
            BP.set_motor_power(left_motor, 0)
            BP.set_motor_power(right_motor, -right_motor_power)
            BP.set_motor_power(left_motor, left_motor_power)
	    print("Currently turning right")
	elif a == "back" or a == "backwards" or a == "BACK" or a == "b" or a == "B":
	    BP.set_motor_power(right_motor, 0)
            BP.set_motor_power(left_motor, 0)
            BP.set_motor_power(right_motor, -right_motor_power)
            BP.set_motor_power(left_motor, -left_motor_power)
	    print ("moving backwards")
        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.






