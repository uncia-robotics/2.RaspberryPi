# ThingSpeak Update Using MQTT
# Compiled by Ashish Kumar 
# www.github.com/ashishk7

from __future__ import print_function
import paho.mqtt.publish as publish
import psutil
import sys
import Adafruit_DHT
import time

# Replace this with your Channel ID
channelID = "573086"
# The Write API Key for the channel
apiKey = "0GVK13PASHPE73AS"

#  MQTT Connection Methods
useUnsecuredTCP = True
useUnsecuredWebsockets = False
useSSLWebsockets = False

# The Hostname of the ThinSpeak MQTT service
mqttHost = "mqtt.thingspeak.com"

# MQTT connection parameters
if useUnsecuredTCP:
    tTransport = "tcp"
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = "websockets"
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    import ssl
    tTransport = "websockets"
    tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
    tPort = 443
        
# Create the topic string
topic = "channels/" + channelID + "/publish/" + apiKey

while(True):
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print("Temperature = %s     Humidity = %s" % (temperature, humidity))
    tPayload = "field1=" + str(temperature) + "&field2=" + str(humidity)
    time.sleep(10)
    try:
        publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)

    except (KeyboardInterrupt):
        break

    except:
        print ("There was an error while publishing the data.")

