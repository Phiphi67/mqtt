import time, board, adafruit_dht
from RPi import GPIO

T=22.0; G=27; R=15
d=adafruit_dht.DHT22(board.D4)
GPIO.setmode(GPIO.BCM)
GPIO.setup((G,R), GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        try:
            t,h=d.temperature,d.humidity
            GPIO.output(R, t<=T)
            GPIO.output(G, t>T)
            print(f"{t:.1f}°C -> {'GREEN' if t<=T else 'RED'}")
            time.sleep(5)
        except RuntimeError:
            time.sleep(2)
finally:
    GPIO.cleanup()

