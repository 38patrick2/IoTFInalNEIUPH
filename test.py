from connection import mqtt_connect
import time

client = mqtt_connect()

client.loop_start()
client.publish("testtopic/1", "100")

time.sleep(2)

client.loop_stop()