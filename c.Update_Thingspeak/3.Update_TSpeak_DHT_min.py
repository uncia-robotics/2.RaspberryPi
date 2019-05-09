# ThingSpeak Update Using MQTT
# written by Ashish Kumar
# www.github.com/ashishk7

from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import sys
import Adafruit_DHT
import time

# The ThingSpeak Channel ID
channelID = "573086"

# The Write API Key for the channel
apiKey = "0GVK13PASHPE73AS"

#MQTT connection methods
Transport = "tcp"
tPort = 1883
tTLS = None

# The Hostname of the ThinSpeak MQTT service
mqttHost = "mqtt.thingspeak.com"
# Create the topic string
topic = "channels/" + channelID + "/publish/" + apiKey

#   using MQTT to update channel with sensor values
while(True):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#    print 'Temp: %s     humidity: %s' % (temperature, humidity)

    tPayload = "field1=" + str(temperature) + "&field2=" + str(humidity)
#    time.sleep(20)
    
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")



