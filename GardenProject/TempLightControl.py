import sys
import Adafruit_DHT as dht
import time
import RPi.GPIO as GPIO
import datetime
import json
import requests

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while(True):

    timer = time.time()

    while(time.time() - timer < 30):


        humidity, temperature = dht.read_retry(dht.DHT11, 22)

        if(temperature < 21):

            GPIO.output(14, GPIO.LOW)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(18, GPIO.HIGH)

        elif(temperature > 29):

            GPIO.output(14, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(18, GPIO.LOW)

        else:

            GPIO.output(14, GPIO.LOW)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)

    url = 'http://garden-project-web-api.herokuapp.com/api/temperatures'
    post_data = {"temperature": "{0:0.2f}".format(float(temperature)),"humidity": "{0:0.2f}".format(float(humidity))}


    #data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=post_data, headers=headers)

    #print("\r\nHOURLY\r\nTemp : {0} \r\nStatus : {1} ".format(float(t11), response.status_code))

    print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)


GPIO.cleanup()
