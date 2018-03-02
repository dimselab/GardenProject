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
import TempLightControl as temp
import _thread as t
import time
import datetime

GPIO.setmode(GPIO.BCM)
"""
Make objects of att the things
ex.
Led1 = led.ExampleClass(control.overlord)
"""
Light = LC.Lights(control.overlord, 18) #Pin 18 to growthLight

UpperWater = water.WaterMeasurer(14) #Pin 14 to Upper Watersensor
LowerWater = water.WaterMeasurer(15) #Pin 15 to Lower Watersensor

WaterPump = pump.Pump(control.overlord, 24, UpperWater) #Pin 24 to Waterpump

Temperature = t.start_new_thread(temp.Temperature, (control.overlord, 17, 27, 23)) #Pin 17, 27, 23, 24 to Temperature

#LAST STEP
t.start_new_thread(control.SetupMQTT,())
while(True):
    if(datetime.datetime.now().time() >= datetime.time(7) and datetime.datetime.now().time() <= datetime.time(17)):
        if(Light.getStatus() == 1):
            Light.notify("lights off")
    if (datetime.datetime.now().time() <= datetime.time(7) and datetime.datetime.now().time()>= datetime.time(17)):
        if (Light.getStatus() == 0):
            Light.notify("lights on")
    if(LowerWater.PumpCheck() == 0):
        on = "pump on"
        WaterPump.notify(on)
    print('Status')
    time.sleep(10)






