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


BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
#BP.BrickPiSetupSensors()

try:

  while True:
      value=BP.get_sensor(BP.PORT_1)
      print(value)
      time.sleep(0.2)  # delay for 0.2 seconds (200ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
      BP.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.

