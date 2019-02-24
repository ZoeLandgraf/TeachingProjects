# This code is largely adapted from: https://github.com/DexterInd/BrickPi/blob/master/Software/BrickPi_Python/

from __future__ import print_function
from __future__ import division
from builtins import input

import time
import utils as utils

# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print(),
# the integer division and input()
# mind your parentheses!

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B

BrickPiSetupSensors() #Send the properties of sensors to BrickPi


#Communication timeout in ms (how long since last valid communication before floating the motors).
#0 disables the timeout so the motor would keep running even if it is not communicating with the RaspberryPi
BrickPi.Timeout=3000
print("BrickPiSetTimeout Status :",BrickPiSetTimeout())



# def dummy(port_input, speed = 50):
#
#     port = utils.getPort(port_input)
#
#     start_motor = None
#     while(not (start_motor == 'g' or start_motor == 'G') ):
#         start_motor = input("Waiting for you to press the 'g' key...")
#
#     print("starting motor at port ", port, "with speed")
#     stop_motor = None


def control_motor_with_keys(port_input, speed=50):

    # get the port using getPort in utils
    port = utils.getPort(port_input)

    # get user input to start motor
    start_motor = None
    while(not (start_motor == 'g' or start_motor == 'G') ):
        start_motor = input("Waiting for you to press the 'g' key...")

    # start motor at speed 'speed'
    print("starting motor at port ", port, "with speed")
    BrickPi.MotorSpeed[port] = speed
    stop_motor = None

    # get user input to start motor
    while (not (stop_motor == 's' or stop_motor == 'S')):
        stop_motor = input("stop me with s")
        BrickPiUpdateValues()

    #stop motor
    BrickPi.MotorSpeed[port] = 0



if __name__ == "__main__":
