import paho.mqtt.client as mqtt

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
    overlord.notify_minions(decodedmessage)

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
            print('Notifying ', minion)
            minion.notify(args)

overlord = Overlord()




