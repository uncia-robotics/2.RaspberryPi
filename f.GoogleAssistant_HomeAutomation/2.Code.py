# Control LED using Google Home Assistant
# written by Ashish Kumar
# www.github.com/ashishk7

import json
import requests
import time
import RPi.GPIO as GPIO
led = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
myserverURL = "https://api.thingspeak.com/channels/577527/feeds.json?api_key=9E9L480OZE16RZSP&results=1"
while(True):
  data=requests.get(myserverURL)
  if data.status_code!=200:
    print("error");
  try:
    data=json.loads(data.text)
  except:
    data=None;
  if data!=None:
    value =data["feeds"][0]["field1"]
    print("value = %s" % (value))
    if value=='1':
        GPIO.output(led,True)
    if value=='0':
        GPIO.output(led,False)
    time.sleep(0.01)

