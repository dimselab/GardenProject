"""
Created by Rasmus Edin Thomasen (Github: https://github.com/Gitgest)
           Nicki Feldt (Github: https://github.com/Lardsoup)

A class meant to control the water-pump.
Water should be checked every hour.
Should turn off pump on an off string received.
Should turn on pump on a on string received.
"""
from RPi import GPIO
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) #set up BOARD GPIO numbering.
import GardenProject.WaterMeasurer as WaterSensor


class Pump(object):

    """ Initializer """
    def __init__(self, overlord, pinname, pinSensor):
        self.pinname = pinname
        GPIO.setup(pinname, GPIO.out)
        overlord.register_minion(self)
        self.pinSensor = pinSensor



    #Notify method should take a command from the MQTT server.
    #Depending on the command it should either turn the pump on or off.
    #Command should also print on or off message to console.
    #(Command should originate from the humidity measurer.)



    def notify(self, command):
        """ Turn on and off output to relay, returns string based on input. """
        if (command.lower() == "pump on"):
            waterSensorCheck = False

            while(waterSensorCheck == False):
                if(waterSensorCheck == False):
                    GPIO.OUTPUT(self.pinname, 1)
                    print('pump turned off')
                    return "pump turned off"
                else:
                    GPIO.OUTPUT(self.pinname, 0)
                    print('pump turned on')
                    return "pump turned on"
                waterSensorCheck == True
                waterSensorCheck == WaterSensor.PumpCheck(self.pinSensor)
"""
        if(command.lower() == "pump off"):
            GPIO.OUTPUT(self.pinname, 0)
            print('pump turned off')
            return "pump turned off"

        elif(command.lower() == "pump on"):
            GPIO.OUTPUT(self.pinname, 1)
            print('pump turned on')
            return "pump turned on"

        else:
            print("unknown command")
            return "unknown command"
"""
