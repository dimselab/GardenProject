"""
Made By: Ricco And Tom
"""

import paho.mqtt.client as mqtt
import _thread
import json
import requests

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

    def rest_post(self, returnMessage):
        if("light" in returnMessage):
            uri = "http://garden-project-web-api.herokuapp.com/api/lights";
            if("on" in returnMessage):
                postData = {"status": 'on'};
            elif("off" in returnMessage):
                postData = {"status": 'off'};
            postHeaders ={'Content-type': 'application/json'};

            response = requests.post(uri, json=postData, headers=postHeaders)


        elif("pump" in returnMessage):
            uri = "";
            postData = {};
            postHeaders ={};
        elif(""):
            print("LOLOLOLOL")
        

overlord = Overlord()




