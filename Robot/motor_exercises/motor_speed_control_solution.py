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


#Communication timeout in ms (how long since last valid communication before floating the motors).
#0 disables the timeout so the motor would keep running even if it is not communicating with the RaspberryPi
BrickPi.Timeout=3000
print("BrickPiSetTimeout Status :",BrickPiSetTimeout())


def test_timeout(port, speed):

    # inform the user that the motor at port "port" is starting with speed value "speed"
    print("Starting motor at port ", port, " with speed ", speed)

    # Set the motor to speed using the BrickPi library command: BrickPi.MotorSpeed[PORT_NUMBER].
    # Choose the correct port according to the input variable 'port'. Valid options are:
    # 'PORT_A', 'PORT_B', 'PORT_C', 'PORT_D'
    # Inform the user in the case that he has choosen a wrong port option
    if port == "PORT_A":
        BrickPi.MotorSpeed[PORT_A] = speed
    elif port == "PORT_B":
        BrickPi.MotorSpeed[PORT_B] = speed
    elif port == "PORT_C":
        BrickPi.MotorSpeed[PORT_C] = speed
    elif port == "PORT_D":
        BrickPi.MotorSpeed[PORT_D] = speed
    else:
        print("invalid port option. Choose 'PORT_A, PORT_B, PORT_C or PORT_D'")


def move_motor_for_seconds(motor, speed, seconds):

    #set the motor speed
    BrickPi.MotorSpeed[PORT_A] = speed

    #get the current time
    current_time = time.time()
    #loop while time difference is < 3

    #solution 1
    time_difference = 0
    while(time_difference < 3):
        new_time = time.time()
        time_difference = new_time - current_time
        BrickPiUpdateValues() # Ask BrickPi to update values for sensors/motors
        time.sleep(.1) # sleep for 100 ms

    # solution 2 (more elegant and concise -> less lines of code)
    while(time.time() - current_time < 3):
        BrickPiUpdateValues() # Ask BrickPi to update values for sensors/motors
        time.sleep(.1) # sleep for 100 ms


if __name__ == "__main__":


    test_timeout("PORT_A", 50);
