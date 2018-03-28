#import library mqtt
import paho.mqtt.client as mqtt_client

#inisiaslsasi client sbg publisher
pas = mqtt_client.Client()

#koneksikan ke broker
pas.connect("127.0.0.1", 1883)

def handle_message(mqttc, obj , msg):
	#dapatkan topik dan payloadnya
	topic = msg.topic 
	payload = msg.payload
	payload = payload.decode('ascii')
	#cetaak ke layar
	print("topik : "+topic+ " Payload : "+payload)
#daftarkan fungsi untuk event on_message
kondisi = input("kondisi : ")
pas.publisher("/sensor/pasien/1", kondisi)

pas.on_message = handle_message
#passcribe ke topic
pas.subscribe("/sensor/dok/1")

#loop forever
pas.loop_forever()