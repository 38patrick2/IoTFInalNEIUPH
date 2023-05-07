import paho.mqtt.client as mqtt

# Define callback functions for connection, subscription, and message received
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))
   
def on_subscribe(client, userdata, mid, granted_qos):
   print("Subscribed to topic")


def on_message(client, userdata, msg):
   print("Topic: "+msg.topic+" | Message: "+str(msg.payload.decode()))


def on_publish(client, userdata, mid):
   print("Message published")


def mqtt_connect():
   client = mqtt.Client()
   client.on_connect = on_connect
   client.on_subscribe = on_subscribe
   client.on_message = on_message
   client.on_publish = on_publish
   client.connect("broker.hivemq.com", 1883, 60)  # replace with your cluster address
   
   return client

