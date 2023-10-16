from paho.mqtt import client

print("Starting my application...")

broker = "localhost" #in the view of the program running on EC2, the MQTT broker is the localhost
port = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    data = msg.payload.decode() #decode received bytes to a string.
    if process_data(data):
        mqtt_client.publish("PETBUZZER", "CAUTION") #downstream sub to PETBUZZER
    print(f"Received" '{data}' from '{msg.topic}' topic")
    processed_data = data + "processed" #publish processed data to data_out
    print(f"Processed data published: '{processed_data}'")

def process_data(self, data):
    data_converted = int(data)
    if data_converted > 25:
        return True
    else 
        return False

mqtt_client = client.Client("my_client")
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
