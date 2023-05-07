import tkinter as tk

from connection import *

# MQTT client setup
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)


# Temperature list
temperatures = []


# Function to get current temperature from Raspberry Pi
def get_current_temp():
   # Code to get current temperature from Raspberry Pi and publish to MQTT topic
   # ...
   # Publish temperature to topic "temp/current"
   client.publish("temp/current", "25.5")


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


# Create tkinter window and widgets
window = tk.Tk()
window.title("Temperature Monitor")


# Create buttons to get current temperature, display average temperature, and clear temperature list
get_temp_button = tk.Button(window, text="Get current temperature", command=get_current_temp)
avg_temp_button = tk.Button(window, text="Display average temperature", command=display_avg_temp)
clear_button = tk.Button(window, text="Clear temperature list", command=clear_temps)


# Create label to display temperature information
temp_label = tk.Label(window, text="")


# Add widgets to window
get_temp_button.pack(pady=10)
avg_temp_button.pack(pady=10)
clear_button.pack(pady=10)
temp_label.pack(pady=10)


# Start tkinter event loop
window.mainloop()







