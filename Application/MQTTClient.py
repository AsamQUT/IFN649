import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish 
import serial 


print("Starting my application...")

broker = "localhost" #in the view of the program running on EC2, the MQTT broker is the localhost
port = 1883

def on_connect(client, userdata, flags, rc):
    subscribe_topic1 = "PETHR"
    subscribe_topic2 = "PETTEMP"
    publish_topic = "PETBUZZER"
    print(f"Connected to MQTT Server: {broker} at port {port}")
    client.subscribe(subscribe_topic1)
    client.subscribe(subscribe_topic2)
    client.publish(publish_topic)
    print(f"Subscribed to topics: {subscribe_topic1}, {subscribe_topic2}")


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    TEMP_data = 25
    HR_DATA = 50
    if msg.topic == "PETTEMP":
        TEMP_data = (payload)
        print(msg.topic + "\nTEMP:" +str(msg.payload.decode("utf-8")))
    elif msg.topic == "PETHR":
        HR_DATA = (payload)
        print(msg.topic + "\nBPM:" +str(msg.payload.decode("utf-8")))
    
        data1 = int(TEMP_data) 
        data2 = int(HR_DATA)
        if (data1 >= 25 and data2 >= 100) or data2 >140:
            publish.single("PETBUZZER", "CAUTION") #downstream sub to PETBUZZER
            print(f"Warning published")
    



        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port, 60)
client.loop_forever()



