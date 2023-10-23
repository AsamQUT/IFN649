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
    client.subscribe(subscribe_topic1) #subscribe to PETHR
    client.subscribe(subscribe_topic2) #subscribe to PETTEMP
    client.publish(publish_topic)
    print(f"Subscribed to topics: {subscribe_topic1}, {subscribe_topic2}")


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    TEMP_data = 20 #set starting value to arbitrary number otherwise will get an error that data value is being called before it is set when trying to check if the client needs to publisher to subscribers
    HR_DATA = 50 #set starting value to arbitrary number otherwise will get an error that data value is being called before it is set when trying to check if the client needs to publisher to subscribers
    if msg.topic == "PETTEMP": #if the topic is PETTEMP then set the payload to TEMP
        TEMP_data = (payload)
        print(msg.topic + "\nTEMP:" +str(msg.payload.decode("utf-8"))) #prints the data value of TEMP
    elif msg.topic == "PETHR": #if the topic is PETHR then set the payload to HR
        HR_DATA = (payload)
        print(msg.topic + "\nBPM:" +str(msg.payload.decode("utf-8"))) #prints the data value of HR
    
        data1 = int(TEMP_data) #convert payload to int
        data2 = int(HR_DATA) #convert payload to int
        if (data1 >= 25 and data2 >= 100) or data2 >140: #check if data threshold is met
            publish.single("PETBUZZER", "CAUTION") #downstream sub to PETBUZZER to set buzzer off
            print(f"Warning published") #print that warning is published
    



        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker,port, 60)
client.loop_forever()



