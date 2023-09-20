import paho.mqtt.client as mqtt
import serial # importa serial lib!

def on_connect(client, userdata, flags, rc): # func for making connection
	print(f"Connected to MQTT Server {ADD} at port {PORT}")
	print("Connection returned result: " +str(rc))
	topic = "ifn649"
	client.subscribe(topic)
	print(f"Subscribed to topic: {topic}")
	
def on_message(client, userdata, msg): # Func for sending msg
	print("Received message!")
	print(msg.topic+" "+str(msg.payload))
	print("relaying to teensy over BT...")
	# Code from last week's bt.py
	# relay the command from Pi to Teensy
	# Connect Pi with Teensy over BT first!
	ser = serial.Serial("/dev/rfcomm0",9600)
	ser.write(msg.payload)

ADD = "ip-address"
PORT = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ADD, PORT, 60)
client.loop_forever()
