"""
Daniel
Philip
Niklas

This module is used to act like a light switch.
it takes a string in the "notify" and turns the light on or off accordingly.
It is initialised by giving it an overlord (the observer that keeps tracks)
and a pin number on the pin that needs to send the signal to the relay.
Calling the notify function needs a "command" and it respectively turns on or off the light,
prints in console what it did and returns it for functions that are waiting for it.
"""
from RPi import GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
class Lights:
    def __init__(self,overlord, pinnumber):
        self.pinnumber = pinnumber
        GPIO.setup(pinnumber, GPIO.OUT)
        overlord.register_minion(self)
    def notify (self, command):
        if (command.lower() == "lights off"):
            GPIO.output(self.pinnumber, 0)
            print( 'Lights turned off')
            return 'Lights turned off'
        elif (command.lower() == "lights on"):
            GPIO.output(self.pinnumber, 1)
            print( "Lights turned on")
            return "Lights turned on"
        else:
            return "Unknown Command"
