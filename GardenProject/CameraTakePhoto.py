# Casper, Rolf og Benjamin - Team older

from picamera import PiCamera
from time import sleep

camera = PiCamera()

class TakeOnePhoto:
    def __init__(self, overlord):
        overlord.register_minion(self)
    #Tager billede naar koert, og gemmer paa det eksisterende.
    def TakePhoto(self):
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
    def notify(self, command):
        if "photo" in str(command).lower():
            TakePhoto()
  