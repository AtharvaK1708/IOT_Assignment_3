import random
import time
import paho.mqtt.publish as publish

# Required api keys and username/passwords
channel_ID = "2892314"
api_key = "5KIS6EHP3RRHIJFH"
mqtt_host = "mqtt3.thingspeak.com"
client_ID = "ExU8OSAhERYVCy4CISQGNRA"  
mqtt_username = "ExU8OSAhERYVCy4CISQGNRA"        
mqtt_password = "ScdqHec5P5JSX2qCR2eGP/sr"        

# creates random values of tempreature, humidity and CO2
def generate_sensor_data():
    Temperature = random.uniform(-50, 50)
    Humidity = random.uniform(0, 100)
    CO2 = random.uniform(300, 2000)
    return Temperature, Humidity, CO2

# function to publish to thingspeak using MQTT
def publish_data(Temperature, Humidity, CO2):
    payload = f"field1={Temperature}&field2={Humidity}&field3={CO2}"
    topic = f"channels/{channel_ID}/publish"

    publish.single(
        topic,
        payload,
        hostname=mqtt_host,
        client_id=client_ID,
        auth={'username': mqtt_username, 'password': mqtt_password}
    )
    print(f"✅ Data sent to ThingSpeak: Temp={Temperature:.2f}, Humidity={Humidity:.2f}, CO2={CO2:.2f}")
   

if __name__ == "__main__":
    while True:
        temp, hum, co2 = generate_sensor_data()
        publish_data(temp, hum, co2)
        time.sleep(60)  # publish after every 1 minute
