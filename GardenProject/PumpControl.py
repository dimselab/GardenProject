"""
A class meant to control the water-pump.
Water should be checked every hour.
Should turn off pump on an off string recieved.
Should turn on pump on a on string recieved.
"""
import RPi.GPIO as GPIO
# setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

class Pump(object):
    name = ""

    """ initializer """
    def __init__(self, name):

        self.name = name # initialize variable.

    def notify(self, str):
        if str == "on":
            print("Pump is turned on")

        elif str =="off":
            print("Pump is turned off")

        self.str = str




