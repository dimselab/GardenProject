from RPi import GPIO
GPIO.cleanup()

class Lights:
    def __init__(self,overlord, pinname):
        self.pinname = pinname
        overlord.register_minion(self)
    def notify (self, command):
        if (command.lower() == "lights off"):
            GPIO.OUTPUT(self.pinname, 0)
            print("Lights turned off")
        elif (command.lower() == "lights on"):
            GPIO.OUTPUT(self.pinname, 1)
            print("Lights turned on")
        else:
            return "Unknown Command"
