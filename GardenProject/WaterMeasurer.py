
import RPi.GPIO as GPIO
global Pin_nr

#Casper, Rolf og Benjamin - Team Older
#Needs the GPIO num for the lvl.
class WaterMeasurer(object):
    def __init__(self, pin_nr):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(port_nr, GPIO.OUT)
        self.Pin_nr = pin_nr

    #returns 1 for true
    # #returns 0 for false
    def PumpCheck(self):
        return GPIO.input(Pin_nr)
