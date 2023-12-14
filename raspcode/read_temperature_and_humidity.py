import Adafruit_DHT
from time import sleep
import requests
sensor = Adafruit_DHT.DHT11

url = 'http://127.0.0.1:8000/plants/update_temp/'

pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    data = {'temperature': temperature, 'air_humidity': humidity}
    requests.put(url, json=data)
    # print(f'Temp={temperature}*C  Humidity={humidity}%')
    sleep(120)

