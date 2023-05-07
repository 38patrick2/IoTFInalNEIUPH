import paho.mqtt.client as mqtt
import time

def mqtt_connect():
   client = mqtt.Client()
   client.username_pw_set("mfejzic2", "Bratunac?13")  # if authentication is required
   client.connect("broker.hivemq.com", 1883)  # replace with your cluster address
   return client

# Define callback functions for connection, subscription, and message received
def on_connect(client, userdata, flags, rc):
   print("Connected with result code "+str(rc))
   client.subscribe("final")


def on_subscribe(client, userdata, mid, granted_qos):
   print("Subscribed to topic")


def on_message( msg):
   print("Topic: "+msg.topic+" | Message: "+str(msg.payload.decode()))


def on_publish(client, userdata, mid):
   print("Message published")


# Create an MQTT client instance
client = mqtt.Client()


# Set the callback functions
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish


# Connect to the HiveMQ broker
client.connect("broker.hivemq.com", 1883, 60)


# Start the network loop
client.loop_start()


# Publish a message to a topic
client.publish("final", "Hello, world!")


# Wait for the message to be received
time.sleep(2)


# Stop the network loop
client.loop_stop()
