

# Adafruit_DHT library imported to run DHT11 temperature and humidity sensors. The script for temperature mesurements uses pin 22. 

#Definition init sets the used pins in the temperature control method. 
#Definition notify is the method that measures temperature and depending on the temp the RGB lamp light up blue, green or red. 


import Adafruit_DHT as dht
from RPi import GPIO
import json
import requests


class Temperature:
    def _init_(self,overlord, pinnumber1, pinnumber2, pinnumber3):
        
        
        GPIO.setup(pinnumber1, GPIO.OUT)
        GPIO.setup(pinnumber2, GPIO.OUT)
        GPIO.setup(pinnumber3, GPIO.OUT)
        overlord.register_minion(self)
    def notify(self, command):
        while (True):

            timer = time.time()

            while (time.time() - timer < 30):

                humidity, temperature = dht.read_retry(dht.DHT11, 22)

                if (temperature < 21):

                    GPIO.output(pinnumber1, GPIO.LOW)
                    GPIO.output(pinnumber2, GPIO.LOW)
                    GPIO.output(pinnumber3, GPIO.HIGH)

                elif (temperature > 29):

                    GPIO.output(pinnumber1, GPIO.HIGH)
                    GPIO.output(pinnumber2, GPIO.LOW)
                    GPIO.output(pinnumber3, GPIO.LOW)

                else:

                    GPIO.output(pinnumber1, GPIO.LOW)
                    GPIO.output(pinnumber2, GPIO.HIGH)
                    GPIO.output(pinnumber3, GPIO.LOW)

            url = 'http://garden-project-web-api.herokuapp.com/api/temperatures'
            post_data = {"temperature": "{0:0.2f}".format(float(temperature)),
                         "humidity": "{0:0.2f}".format(float(humidity))}

          
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, json=post_data, headers=headers)

            

            print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)




