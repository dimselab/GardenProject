"""
Daniel
Philip
Niklas
"""
from RPi import GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
class Lights:
    def __init__(self,overlord, pinname):
        self.pinname = pinname
        GPIO.setup(pinname, GPIO.OUT)
        overlord.register_minion(self)
    def notify (self, command):
        if (command.lower() == "lights off"):
            GPIO.output(self.pinname, 0)
            print( 'Lights turned off')
            return 'Lights turned off'
        elif (command.lower() == "lights on"):
            GPIO.output(self.pinname, 1)
            print( "Lights turned on")
            return "Lights turned on"
        else:
            return "Unknown Command"
