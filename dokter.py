#import library mqtt
import paho.mqtt.client as mqtt_client

#inisiaslsasi client sbg publisher
dok = mqtt_client.Client()

#koneksikan ke broker
dok.connect("127.0.0.1", 1883)

def handle_message(mqttc, obj , msg):
	#dapatkan topik dan payloadnya
	topic = msg.topic 
	payload = msg.payload
	payload = payload.decode('ascii')
	#cetaak ke layar
	print("topik : "+topic+ " Payload : "+payload)
	saran = input("saran : ")
#daftarkan fungsi untuk event on_message
dok.on_message = handle_message

dok.subscribe("/sensor/pasien/1")
#dokscribe ke topic
dok.publisher("/sensor/dok/#", saran)
#loop forever
dok.loop_forever()