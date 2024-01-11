from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED
import Adafruit_DHT
from rest_framework.response import Response
# from django.utils import timezone
import requests
from datetime import datetime



def use_pump_and_save(base_url, now):
    pump = LED(18)
    pump.on()
    pump.off()
    sleep(15)
    requests.put(url=base_url+'update_date/', data={'last_watering':now})        


def water_plants():
    i2c_bus = board.I2C()
    
    ss = Seesaw(i2c_bus, addr=0x36)
    base_url = 'http://192.168.0.222:8000/plants/'
    plant_type = requests.get(url=base_url+'get_type/').json()
    print(plant_type)
    last_watering = requests.get(url=base_url+'get_date').json()
    print(type(last_watering['last_watering']))
    now = datetime.now()
    print(now)
    print(type(now))
    hum = ss.moisture_read()
    temp = ss.get_temp()

    if str(plant_type).lower() == 'kawa':
    
        if int(hum) < 400:
            use_pump_and_save(base_url=base_url, now=now)
    
    if plant_type['plant_specie'].lower() == 'kaktus':
        if int(hum) < 400:
            if last_watering['last_watering'] != 0:
                if int(last_watering['last_watering'][8:10]) < int(now.strftime("%d/%m/%Y %H:%M:%S")[3:5]):
                    use_pump_and_save(base_url=base_url, now=now)
            else:
                use_pump_and_save(base_url=base_url, now=now)


if __name__ == '__main__':
    water_plants()




    

