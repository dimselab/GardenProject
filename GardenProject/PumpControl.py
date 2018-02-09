"""
A class meant to control the water-pump.
Water should be checked every hour.
Should turn off pump on an off string recieved.
Should turn on pump on a on string recieved.
"""
from RPi import GPIO
# from MQTTControl import overlord
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD) #set up BOARD GPIO numbering.
GPIO.setup(22, GPIO.OUT) #set up GPIO 22 as output.


class Pump(object):

    """ Initializer """
    def __init__(self,pinname):
        self.name = pinname
        #overlord.register_minion(self)

    def __str__(self):
        return self.name

    """ 
    Notify method should take a command from the MQTT server.
    Depending on command it should either turn the pump on or off.
    Command should originate from the humidity measurer.
    """
    def notify(self, command):
        if(command == "Pump ON"):
            GPIO.OUTPUT(self.pinname, 0)
        elif(command == "Pump OFF"):
            GPIO.OUTPUT(self.pinname, 1)
        else:
            return "Unknown command"



