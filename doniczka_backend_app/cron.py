from adafruit_seesaw.seesaw import Seesaw
from time import sleep
import board
from gpiozero import LED
import Adafruit_DHT
# from models import Plant
from rest_framework.response import Response
# from serializers import LastWateringSerializer
from django.utils import timezone
from doniczka_backend_app.models import Plant
from doniczka_backend_app.serializers import LastWateringSerializer



def use_pump_and_save(plant, now):
    pump = LED(18)
    pump.on()
    pump.off()
    sleep(15)        
    serializer = LastWateringSerializer(instance=plant, data={'last_watering': now})       
    serializer.is_valid(raise_exception=True)
    serializer.save()


def water_plants():
    i2c_bus = board.I2C()
    
    ss = Seesaw(i2c_bus, addr=0x36)
    plant = Plant.objects.get(id=1)
    plant_type = plant.plant_specie
    now = timezone.now
    hum = ss.moisture_read()
    temp = ss.get_temp()

    if str(plant_type).lower() == 'kawa':
    
        if int(hum) < 400:
            use_pump_and_save(plant=plant, now=now)
    
    if str(plant_type).lower() == 'kaktus':
        if int(hum) < 400:
            if plant.last_watering != 0:
                if int(plant.last_watering[8:10]) < int(now)[8:10]:
                    use_pump_and_save(plant=plant, now=now)
            else:
                use_pump_and_save(plant=plant, now=now)


if __name__ == '__main__':
    water_plants()




    

