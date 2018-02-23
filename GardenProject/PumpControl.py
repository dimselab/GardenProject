"""
Created by Rasmus Edin Thomasen (Github: https://github.com/Gitgest)
           Nicki Feldt (Github: https://github.com/Lardsoup)

A class meant to control the water-pump.
Water should be checked every hour.
Should turn off pump on an off string received.
Should turn on pump on a on string received.
"""
from RPi import GPIO
import time


class Pump(object):

    """ Initializer """
    def __init__(self, overlord, pinname, Uppermeasure):
        self.pinname = pinname
        GPIO.setup(pinname, GPIO.OUT)
        overlord.register_minion(self)
        self.LocalUppermeasure = Uppermeasure



    #Notify method should take a command from the MQTT server.
    #Depending on the command it should either turn the pump on or off.
    #Command should also print on or off message to console.
    #(Command should originate from the humidity measurer.)



    def notify(self, command):
        """ Turn on and off output to relay, returns string based on input. """
        if (command.lower() == "pump on"):
            waterSensorCheck = 0

            while(waterSensorCheck == 0):
                waterSensorCheck = 1
                waterSensorCheck = self.LocalUppermeasure.PumpCheck()
                if(waterSensorCheck == 0):
                    GPIO.output(self.pinname, 1)
                    print('pump turned on')
                else:
                    GPIO.output(self.pinname, 0)
                    print('pump turned off')
                time.sleep(0.5)
