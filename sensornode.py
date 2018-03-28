#import library mqtt
import paho.mqtt.client as mqtt_client
import json
import random
import sys

#inisiaslsasi client sbg publisher
pub = mqtt_client.Client()

#koneksikan ke broker
pub.connect("127.0.0.1", 1883)

suhu = randint(-10,50)
lembab = randint(0,100)
co = randint(0,100)
#publish message
pub.publish("sensor/suhu", str(suhu))
pub.publish("sensor/kelembaban", str(lembab)+"%")
pub.publish("sensor/CO", str(co)+"%")