from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED
import Adafruit_DHT
from .serializers import PlantModelSerializer,PlantCreatingSerializer, TemperatureandHumiditySerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Plant
from django_cron import CronJobBase, Schedule

def water_plants():
    i2c_bus = board.I2C()

    ss = Seesaw(i2c_bus, addr=0x36)

    hum = ss.moisture_read()
    temp = ss.get_temp()
    if int(hum) > 400:
        pump = LED(18)
        print('test')
        pump.on()
        pump.off()
        sleep(15)
    print("temp: " + str(temp) + "  moisture: " + str(hum))



class WaterPlants(CronJobBase):
    RUN_EVERY_MINS = 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'doniczka_backend_app.WaterPlants'

    def do(self):
        i2c_bus = board.I2C()

        ss = Seesaw(i2c_bus, addr=0x36)

        hum = ss.moisture_read()
        temp = ss.get_temp()
        if int(hum) > 400:
            pump = LED(18)
            print('test')
            pump.on()
            pump.off()
            sleep(15)
        print("temp: " + str(temp) + "  moisture: " + str(hum))

class CheckHumAndTemperature(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'doniczka_backend_app.CheckHumAndTemperature'

    def do(self):
        pin = 4
        sensor = Adafruit_DHT.DHT11
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        data = {'temperature': temperature, 'air_humidity': humidity}
        # print(f'Temp={temperature}*C  Humidity={humidity}%')
        serializer = TemperatureandHumiditySerializer(instance=Plant.objects.get(id=1), data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('Saved')
    

