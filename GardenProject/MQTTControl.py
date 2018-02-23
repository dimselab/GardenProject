"""
Made By: Ricco And Tom
"""

import paho.mqtt.client as mqtt
import _thread


def SetupMQTT():
    Server_Adress = "192.168.3.144";
    client = mqtt.Client("GardenController");
    client.on_message=on_message;
    client.connect(Server_Adress);
    client.subscribe("/GardenProject");
    client.loop_forever();

def on_message(client, userdata, message):

    decodedmessage = message.payload.decode("utf-8")
    print("message received %s : %s " % (message.topic, decodedmessage))

    _thread.start_new_thread(overlord.notify_minions, (decodedmessage,))

class Overlord:
    def __init__(self):
        self.__minions = []

    def register_minion(self, minion):
        self.__minions.append(minion)

    def notify_minions(self, args):
        print('Notifying minions...')
        print(args)
        print(self.__minions)
        for minion in self.__minions:
            print('Notifying ', str(minion))
            self.status = minion.notify(args)

overlord = Overlord()




