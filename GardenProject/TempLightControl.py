import sys

# Adafruit_DHT library imported to run DHT22 and DHT11 temperature and humidity sensors.

import Adafruit_DHT as dht
import time
import datetime
import RPi.GPIO as GPIO
import threading
from threading import Thread

#Light function currently doing disco ligthing to brighten your day.

def lys_func():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)

    count = 0
    while (count < 100):
        count = count + 1
        GPIO.output(14, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(0.05)
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(15, GPIO.LOW)
        time.sleep(0.05)
        GPIO.output(18, GPIO.HIGH)


#Cleanup of pins signals.
GPIO.cleanup()

#Temperature function currently including both output code for DHT22 and DHT11.

def temp_func():
    humidity, temperature = dht.read_retry(dht.DHT22, 4)
    print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity)

    h11, t11 = dht.read_retry(dht.DHT11, 22)
    print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t11, h11)


#Threading to run more than 1 function in a script.

try:
    Thread(target=temp_func).start()
    Thread(target=lys_func).start()

except:
    print("Threading failed!!!!!!!")
