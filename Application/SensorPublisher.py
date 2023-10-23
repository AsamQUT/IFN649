import serial
import time
import string
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

#reading and writing_data from and to arduino serially.
#rfcomm0 -> this could be different
ser1 = serial.Serial("/dev/rfcomm0",9600)
ser1.write(str.encode('Start\r\n'))

ser2 = serial.Serial("/dev/rfcomm1",9600)
ser2.write(str.encode('Start\r\n'))

while True:
	if ser1.in_waiting > 0:
		rawserial1 = ser1.readline()
		cookedserial1 = rawserial1.decode('utf-8').strip('\r\n')
		publish.single("PETHR", (cookedserial1), hostname="13.239.112.115") #publish data value to topic

		
	if ser2.in_waiting > 0:
		rawserial2 = ser2.readline()
		cookedserial2 = rawserial2.decode('utf-8').strip('\r\n')
		publish.single("PETTEMP", (cookedserial2), hostname="13.239.112.115") #publish data value to topic
	time.sleep(1.5)	#wait for 1.5s 
	



ADD = "13.239.112.115"
PORT = 1883

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ADD, PORT, 60)
client.loop_forever()
