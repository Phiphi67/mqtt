#!/usr/bin/env python3
import time, board, adafruit_dht
import paho.mqtt.client as mqtt

BROKER = "10.100.240.11"
PORT   = 1883
TOPIC_TEMP = "house/dht22/temperature"
USERNAME = "pi"
PASSWORD = "test"

dht = adafruit_dht.DHT22(board.D4)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "TempPublisher")
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        try:
            t = dht.temperature
            client.publish(TOPIC_TEMP, f"{t:.1f}")
            print(f"PUB sent {t:.1f}°C")
            time.sleep(5)
        except RuntimeError:
            time.sleep(2)

finally:
    client.loop_stop()
    client.disconnect()
