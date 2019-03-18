import numpy as np
from BrickPi import *   #import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication


def getPort(port_string):

    if port_string == "PORT_A":
        return PORT_A
    elif port_string == "PORT_B":
        return PORT_B
    elif port_string == "PORT_C":
        return PORT_C
    elif port_string == "PORT_D":
        return PORT_D
    else:
        return "invalid port option. Choose 'PORT_A, PORT_B, PORT_C or PORT_D'"
