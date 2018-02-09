from RPi import GPIO
#from MQTTControl import overlord
GPIO.cleanup()

class Lights:
    def __init__(self,pinname):
        self.name = pinname
        #overlord.register_minion(self)
    def __str__(self):
        return self.name
    def notify(self, command):
        if (command == "Lights OFF"):
            GPIO.OUTPUT(self.pinname, 0)
        elif (command == "Lights ON"):
            GPIO.OUTPUT(self.pinname, 1)
        else:
            return "Unknown Command"
