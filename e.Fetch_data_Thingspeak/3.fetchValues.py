# Fetch data from ThingSpeak Channel
# Written by Ashish Kumar
# www.github.com/ashishk7

import json
import requests
myserverURL = "https://api.thingspeak.com/channels/573086/feeds.json?api_key=1135FZD12JH7HP5P&results=1"

data=requests.get(myserverURL)
if data.status_code!=200:
    print("error");
try:
    data=json.loads(data.text)
except:
    data=None;
if data!=None:
    temperature =data["feeds"][0]["field1"]
    humidity    =data["feeds"][0]["field2"]
    print("Temperature = %s     Humidity = %s" % (temperature, humidity))
    
