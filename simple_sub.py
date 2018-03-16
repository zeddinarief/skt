#import library mqtt
import paho.mqtt.client as mqtt_client

#inisiaslsasi client sbg publisher
sub = mqtt_client.Client()

#koneksikan ke broker
sub.connect("127.0.0.1", 1883)

def handle_message(mqttc, obj , msg):
	#dapatkan topik dan payloadnya
	topic = msg.topic 
	payload = msg.payload
	payload = payload.decode('ascii')
	#cetaak ke layar
	print("topik : "+topic+ " Payload : "+payload)

#daftarkan fungsi untuk event on_message
sub.on_message = handle_message

#subscribe ke topic
sub.subscribe("/sensor/#")

#loop forever
sub.loop_forever()