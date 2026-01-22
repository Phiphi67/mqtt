#!/usr/bin/env python3
from RPi import GPIO
import paho.mqtt.client as mqtt

BROKER = "10.100.240.11"
PORT   = 1883
TOPIC_TEMP = "house/dht22/temperature"
USERNAME = "pi"
PASSWORD = "test"

T = 22.0
G = 27
R = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup((G,R), GPIO.OUT, initial=GPIO.LOW)

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC_TEMP)

def on_message(client, userdata, msg):
    t = float(msg.payload.decode())

    GPIO.output(R, t <= T)
    GPIO.output(G, t > T)

    print(f"SUB received {t:.1f}°C -> {'GREEN' if t<=T else 'RED'}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "TempSubscriber")
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT)

try:
    client.loop_forever()
finally:
    GPIO.cleanup()