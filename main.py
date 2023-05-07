import tkinter as tk

from connection import mqtt_connect
import time

temperatures = []

def on_message(client, userdata, msg):
   print("Topic: "+msg.topic+" | Message: "+str(msg.payload.decode()))
   if msg.topic == "testtopic/1":
      try:
         temperatures.append(int(msg.payload.decode()))
      except ValueError:
         pass
      
client = mqtt_connect()
client.on_message = on_message
client.loop_start()

client.subscribe("testtopic/1")
time.sleep(2)

# Function to get current temperature from Raspberry Pi
def get_current_temp():
   # Code to get current temperature from Raspberry Pi and publish to MQTT topic
   # ...
   # Publish temperature to topic "temp/current"
   # client.publish("temp/current", "25.5")
   client.publish("testtopic/1", "200")

# Function to display average temperature based on list of prior temperatures
def display_avg_temp():
   if len(temperatures) > 0:
       avg_temp = sum(temperatures) / len(temperatures)
       temp_label.config(text="Average temperature: {:.2f} °C".format(avg_temp))
   else:
       temp_label.config(text="Temperature list is empty")

# Function to clear temperature list
def clear_temps():
   temperatures.clear()
   temp_label.config(text="Temperature list cleared")
def display7s():
    pass
# Create tkinter window and widgets
window = tk.Tk()
window.title("Temperature Monitor")


# Create buttons to get current temperature, display average temperature, and clear temperature list
get_temp_button = tk.Button(window, text="Get current temperature", command=get_current_temp)
avg_temp_button = tk.Button(window, text="Display average temperature", command=display_avg_temp)
clear_button = tk.Button(window, text="Clear temperature list", command=clear_temps)
display7s_button = tk.Button(window, text="Display x on the Seven-segment", command=display7s)


# Create label to display temperature information
temp_label = tk.Label(window, text="")


# Add widgets to window
get_temp_button.pack(pady=10)
avg_temp_button.pack(pady=10)
clear_button.pack(pady=10)
display7s_button.pack(pady=10)
temp_label.pack(pady=10)



# Start tkinter event loop
window.mainloop()

client.loop_stop()







