# This code is largely adapted from: https://github.com/DexterInd/BrickPi/blob/master/Software/BrickPi_Python/

from __future__ import print_function
from __future__ import division
from builtins import input

# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print(),
# the integer division and input()
# mind your parentheses!

from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.MotorEnable[PORT_A] = 1 #Enable the Motor A
BrickPi.MotorEnable[PORT_B] = 1 #Enable the Motor B

BrickPiSetupSensors() #Send the properties of sensors to BrickPi


# Communication timeout in ms (how long since last valid communication before floating the motors).
# 0 disables the timeout so the motor would keep running even if it is not communicating with the RaspberryPi
BrickPi.Timeout=3000
print("BrickPiSetTimeout Status :",BrickPiSetTimeout())


def test_timeout(port, speed):

    # Inform the user that the motor at port "port" is starting with speed value "speed"


    # Set the motor to speed using the BrickPi library command: BrickPi.MotorSpeed[PORT_NUMBER].
    # Choose the correct port according to the input variable 'port'. Valid options are:
    # 'PORT_A', 'PORT_B', 'PORT_C', 'PORT_D'
    # Inform the user in the case that he has choosen a wrong port option



def move_motor_for_seconds(motor, speed, seconds):

    # set the motor speed using BrickPi library command BrickPi.MotorSpeed[PORT_A]

    # get the current time

    # loop while time difference is < 3

    # solution 1

    # solution 2 (more elegant and concise -> less lines of code)



if __name__ == "__main__":


    test_timeout("PORT_A", 50);
