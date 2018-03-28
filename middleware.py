#import library mqtt
import paho.mqtt.client as mqtt_client
import json
import threading
import xmlrpc.server

server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )
#inisiaslsasi client sbg publisher
sub = mqtt_client.Client()

#koneksikan ke broker
sub.connect("127.0.0.1", 1883)

sensor = []
def handle_message(mqttc, obj , msg):
	#dapatkan topik dan payloadnya
	
	topic = msg.topic 
	payload = msg.payload
	payload = payload.decode('ascii')
	#cetaak ke layar
	print("topik : "+topic+ " Payload : "+payload)
	sensor_baru = {
		"topik" : topic,
		"payload" : payload
	}
	sensor.append(sensor_baru)

#daftarkan fungsi untuk event on_message
sub.on_message = handle_message

def handle_thread():

	def getAllsensor():
		return json.dumps(sensor)
	def getsensorsuhu():
		for i in range(0, len(sensor)):
	        if sensor[i]["topik"] == "sensor/suhu":
	            return json.dumps(sensor[i])

	def getsensorkelembaban():
		for i in range(0, len(sensor)):
	        if sensor[i]["topik"] == "sensor/kelembaban":
	            return json.dumps(sensor[i])

	def getsensorCO():
		for i in range(0, len(sensor)):
	        if sensor[i]["topik"] == "sensor/suhu":
	            return json.dumps(sensor[i])

	server.register_function(getAllsensor, 'getAllsensor')
	server.register_function(getsensorsuhu, 'getsensorsuhu')
	server.register_function(getsensorkelembaban, 'getsensorkelembaban')
	server.register_function(getsensorCO, 'getsensorCO')
	server.serve_forever()            
            

t = threading.Thread(target=handle_thread)
#start thread
t.start()
sub.subscribe("sensor/#")

sub.loop_forever()

#loop forever
print("loop sub")