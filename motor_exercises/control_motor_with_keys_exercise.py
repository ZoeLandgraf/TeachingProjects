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


from Tutoring.BrickPi3.Software.Python import brickpi3 as bp

BP = bp.BrickPi3()

right_motor_power = 20
left_motor_power = 20
right_motor = BP.PORT_C
left_motor = BP.PORT_A

try:
    while True:

        a = input()

        if a == "G" or "g":
            BP.set_motor_power(right_motor, right_motor_power)
            BP.set_motor_power(left_motor, left_motor_power)
            print("Moving forward at speed ", right_motor_power)
            a = "I" #i for idle, don't do anything but wait for next input

        if a == "S" or "s":
            BP.set_motor_power(right_motor, 0)
            BP.set_motor_power(left_motor, 0)
            print("Stopped")
            a = "I"  # i for idle, don't do anything but wait for next input

        time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.






