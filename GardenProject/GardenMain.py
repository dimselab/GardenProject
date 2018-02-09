"""
Import All "Things"
ex.
import Mqtt.LEDTEST as led
"""
import MQTT.MQTTControl as control
import MQTT.LightControl as LC


"""
Make objects of att the things
ex.
Led1 = led.ExampleClass(control.overlord)
"""
Light = LC.Lights(control.overlord, 14)

#LAST STEP
control.SetupMQTT()




