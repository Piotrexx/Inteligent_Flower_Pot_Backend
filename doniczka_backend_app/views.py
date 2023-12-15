from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Plant
from .serializers import PlantModelSerializer,PlantCreatingSerializer, TemperatureandHumiditySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
import Adafruit_DHT
from gpiozero import LED
from time import sleep


class PlantViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Plant.objects.all()
    serializer_class = PlantModelSerializer
    sensor = Adafruit_DHT.DHT11
    pin = 4
    led = LED(18)
    
    @action(detail=False, methods=['post'])
    def create_plant(self,request):
        serialzier = PlantCreatingSerializer(data=request.data)
        serialzier.is_valid(raise_exception=True)
        serialzier.save()
        return Response('Roślina zasadzona ;D')

    # @action(detail=False, methods=['put'])
    # def update_temp(self, request):
    #     humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
    #     serializer = TemperatureandHumiditySerializer(data={'temperature':temperature, 'air_humidity':humidity})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('Temperatura zaktualizowana')
    
    @action(detail=True, methods=['get'])
    def get_info(self,request, pk):
        try:
            get_object_or_404(Plant, id=pk)
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            serializer = TemperatureandHumiditySerializer(instance=Plant.objects.get(id=pk), data={'temperature':temperature, 'air_humidity':humidity})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(self.serializer_class(Plant.objects.get(id=pk)).data, status=HTTP_200_OK)
        except:
            return Response('Roślina nie znaleziona :(', status=HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])
    def water_the_plants(self, request):
        self.led.on()
        sleep(5)
        self.led.off()
        return Response('Podlane !')