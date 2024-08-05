# The following example is derived from
# the official example at https://pypi.org/project/paho-mqtt/
import paho.mqtt.client as mqtt
import ssl
import struct


def on_connect(client, userdata, flags, rc, properties):
    print("Connected to the broker.")
    client.subscribe("to_client", 0)

def on_message(client, userdata, msg):
    print("Received (topic '" + msg.topic + "'): " + str(msg.payload, encoding='utf8'))
    print("Type your message to publish: ", end='')
    msg = input()
    client.publish(tp, msg, 0) # first argument is topic; second, qos level

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"unique ID")
client.on_connect = on_connect
client.on_message = on_message
# Use the username and password for your group
client.username_pw_set("YOUR_ID", "YOUR_PSSWORD")
client.connect("140.122.185.98", 1883, 60)

tp = "to_server"
print("Type your message to publish: ", end='')
msg = input()
client.publish(tp, msg, 0) # first argument is topic; second, qos level
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
