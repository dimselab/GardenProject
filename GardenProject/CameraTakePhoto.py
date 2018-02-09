from picamera import PiCamera
from time import sleep
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/older")

camera = PiCamera()

##camera.start_preview()
##for i in range(5):
##    sleep(2)
##    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
##camera.stop_preview()

#Tager billede naar koert, og gemmer paa det eksisterende.
def TakePhoto():
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if "photo" in str(msg.payload).lower():
        TakePhoto()

    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Husk at opdatere Ebbe Ip addresse til mqtt server.
client.connect("192.168.3.144", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()