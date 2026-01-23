import time, board, adafruit_dht
from RPi import GPIO

# Schwellenwert und GPIO-Pins definieren
T=22.0; G=27; R=15
# DHT22-Sensor initialisieren
d=adafruit_dht.DHT22(board.D4)
# GPIO-Modus und Ausgangspins konfigurieren
GPIO.setmode(GPIO.BCM)
GPIO.setup((G,R), GPIO.OUT, initial=GPIO.LOW)

try:
    # Endlosschleife zur Temperaturüberwachung
    while True:
        try:
            # Temperatur und Feuchtigkeit messen
            t,h=d.temperature,d.humidity
            # LEDs basierend auf Temperatur schalten
            GPIO.output(R, t<=T)
            GPIO.output(G, t>T)
            print(f"{t:.1f}°C -> {'GREEN' if t<=T else 'RED'}")
            time.sleep(5)
        except RuntimeError:
            # Fehler beim Lesen ignorieren und kurz warten
            time.sleep(2)
finally:
    GPIO.cleanup()

