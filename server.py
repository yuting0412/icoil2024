# The following example is derived from
# the official example at https://pypi.org/project/paho-mqtt/
import paho.mqtt.client as mqtt
import ssl
import struct
import time


def on_connect(client, userdata, flags, rc, properties):
    print("Connected to the broker.")

def on_message(client, userdata, msg):
    payload_string = str(msg.payload, encoding='utf8')
    print("Received (topic '" + msg.topic + "'): " + payload_string)
    # performing some work (sleep)...
    time.sleep(1)
    client.publish("to_client", "Message from the server: I've got your message, namely '" + payload_string +"'", 0) # first argument is topic; second, qos level

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"unique ID")
client.on_connect = on_connect
client.on_message = on_message
# Use the username and password for your group
client.username_pw_set("YOUR_ID", "YOUR_PSSWORD")
client.connect("140.122.185.98", 1883, 60)
client.subscribe("to_server", 0)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
