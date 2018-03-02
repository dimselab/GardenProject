

# Adafruit_DHT library imported to run DHT22 and DHT11 temperature and humidity sensors.

#Definition init sets the used pins in the temperature control method. 
#Definition notify is the method that measures temperature and depending on the temp the RGB lamp light up blue, green or red. 


import Adafruit_DHT as dht
from RPi import GPIO
import json
import requests


class Temperature:
    def _init_(self,overlord):
        GPIO.setup(14, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        overlord.register_minion(self)
    def notify(self, command):
        while (True):

            timer = time.time()

            while (time.time() - timer < 30):

                humidity, temperature = dht.read_retry(dht.DHT11, 22)

                if (temperature < 21):

                    GPIO.output(14, GPIO.LOW)
                    GPIO.output(15, GPIO.LOW)
                    GPIO.output(18, GPIO.HIGH)

                elif (temperature > 29):

                    GPIO.output(14, GPIO.HIGH)
                    GPIO.output(15, GPIO.LOW)
                    GPIO.output(18, GPIO.LOW)

                else:

                    GPIO.output(14, GPIO.LOW)
                    GPIO.output(15, GPIO.HIGH)
                    GPIO.output(18, GPIO.LOW)

            url = 'http://garden-project-web-api.herokuapp.com/api/temperatures'
            post_data = {"temperature": "{0:0.2f}".format(float(temperature)),
                         "humidity": "{0:0.2f}".format(float(humidity))}

            # data_json = json.dumps(data)
            headers = {'Content-type': 'application/json'}
            response = requests.post(url, json=post_data, headers=headers)

            # print("\r\nHOURLY\r\nTemp : {0} \r\nStatus : {1} ".format(float(t11), response.status_code))

            print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)




