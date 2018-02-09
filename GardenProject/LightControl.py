from RPi import GPIO
GPIO.cleanup()

class Lights:
    def __init__(self,overlord, pinname):
        self.pinname = pinname
        overlord.register_minion(self)
    def notify (self, command):
        if (command.lower() == "Lights OFF"):
            GPIO.OUTPUT(self.pinname, 0)
            "Lights turned off"
        elif (command.lower() == "Lights ON"):
            GPIO.OUTPUT(self.pinname, 1)
        else:
            return "Unknown Command"
