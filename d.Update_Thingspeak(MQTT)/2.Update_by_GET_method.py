# Program to update Thingspeak Channel with temperature and humidity values using DHT11 or DHT22 sensor
# written and compiled by Ashish Kumar
# www.githhub.com/ashishk7

import json
import requests
import time
import sys
import Adafruit_DHT

API =  "0GVK13PASHPE73AS"   # enter you Thingspeak Write API key here
while(True):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)  #11=DHT11, 4=GPIO4
    print("Temperature = %s     Humidity = %s" % (temperature, humidity))
    payload = "https://api.thingspeak.com/update?api_key=" + str(API)+ "&" + "field1=" + str(temperature) + "&field2=" + str(humidity)
    data=requests.get(payload)

    if data.status_code!=200:
        print("error!!! uploading")
    else:
        print("uploaded to server sucessfully")

