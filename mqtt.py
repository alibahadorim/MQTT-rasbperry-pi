import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import json

# Define the MQTT broker address and topic
broker_address = "172.20.10.8"
topic = "house/sensors"

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address)

# Create an instance of the Sense HAT
sense = SenseHat()

# Read the temperature and humidity from the Sense HAT sensors
temperature = round(sense.get_temperature(), 2)
humidity = round(sense.get_humidity(), 2)

# Create a string containing the sensor data
sensor_string = "Temperature: {} C\nHumidity: {} %".format(temperature, humidity)

# Print the sensor data to the console
print("+--------------+")
print("|  SENSOR DATA |")
print("+--------------+")
print(sensor_string)

# Publish the sensor data to the MQTT broker
client.publish(topic, sensor_string)

# Create a dictionary containing the sensor data
sensor_data = {"temperature": temperature, "humidity": humidity}

# Convert the dictionary to a JSON string
json_data = json.dumps(sensor_data)

# Publish the JSON string to the MQTT broker
client.publish(topic, json_data)

# Disconnect from the MQTT broker
client.disconnect()
