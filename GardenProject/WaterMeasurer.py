
import RPi.GPIO as GPIO
global Pin_nr

#Casper, Rolf og Benjamin - Team Older
#Needs the GPIO num for the lvl.
class WaterMeasurer(object):
    def __init__(self, pin_nr):
        GPIO.setup(pin_nr, GPIO.IN)
        self.Pin_nr = pin_nr

    #returns 1 for true
    # #returns 0 for false
    def PumpCheck(self):
        print(GPIO.input(self.Pin_nr))
        return GPIO.input(self.Pin_nr)
