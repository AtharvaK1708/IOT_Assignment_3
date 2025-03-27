# IOT Assignment 3

Name: Atharva Kulkarni
SUID: 782904050
Email: akulka15@syr.edu

Steps taken for the assignment: 

* The first step was to create an account on ThingSpeak and Create a new channel to create an MQTT connection. 
* I had to create a new MQTT device in ThingSpeak and authorize the new created channel to be able to use the MQTT protocol without which ThingSpeak uses HTTP protocol
* Once ThingSpeak was setup and I got the write and read API keys the next step was to code the simulation of the virtual sensors using python.
* I used python because of my familiarity with it and easy library access to use MQTT
* In the code “publish_code.py” the first function generates random data simulating the virtual sensors.
* The second function connects with ThingSpeak using MQTT and publishes the generated sensor data.
* Both these functions are called when the program is run and the data is published every 1 minute.
* In python I used the paho-mqtt library to get access to the publish function which sent the data to ThingSpeak through MQTT
