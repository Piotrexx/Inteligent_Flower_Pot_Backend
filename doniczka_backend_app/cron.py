from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED
import Adafruit_DHT
from .serializers import GroundHumiditySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Plant

def water_plants():
    i2c_bus = board.I2C()
    
    ss = Seesaw(i2c_bus, addr=0x36)

    hum = ss.moisture_read()
    temp = ss.get_temp()
    try:
        get_object_or_404(Plant.objects.get(id=1))
        serializer = GroundHumiditySerializer(instance=Plant.objects.get(id=1), data={'ground_humidity':hum})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        if int(hum) < 400:
            pump = LED(18)
            print('test')
            pump.on()
            pump.off()
            sleep(15)
    except:
        print('Trzeba zrobić roślinę')

        
    print("temp: " + str(temp) + "  moisture: " + str(hum))



    

