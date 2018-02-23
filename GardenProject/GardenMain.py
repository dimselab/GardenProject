"""
Made By: Ricco And Tom
"""

"""
Import All "Things"
ex.
import Mqtt.LEDTEST as led
"""
import RPi.GPIO as GPIO
import MQTTControl as control
import LightControl as LC
import PumpControl as pump
import WaterMeasurer as water
import _thread as t
import time

GPIO.setmode(GPIO.BCM)
"""
Make objects of att the things
ex.
Led1 = led.ExampleClass(control.overlord)
"""
Light = LC.Lights(control.overlord, 18)

UpperWater = water.WaterMeasurer(14)
LowerWater = water.WaterMeasurer(15)

WaterPump = pump.Pump(control.overlord, 23, UpperWater)


#LAST STEP
t.start_new_thread(control.SetupMQTT,())
while(True):
    if(LowerWater.PumpCheck() == 1):
        on = "pump on"
        WaterPump.notify(on)
    print('Status')
    time.sleep(10)






