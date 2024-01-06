from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Plant
from .serializers import PlantModelSerializer,PlantEditingSerializer,PlantCreatingSerializer, TemperatureandHumidityWaterLevelSerializer, LastWateringSerializer, GetFlowerTypeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT, HTTP_201_CREATED
import Adafruit_DHT
from gpiozero import LED, Button
from time import sleep
from raspcode.checking_water_level import check_water_level

class PlantViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Plant.objects.all()
    serializer_class = PlantModelSerializer
    sensor = Adafruit_DHT.DHT11
    pin = 4

    
    @action(detail=False, methods=['post'])
    def create_plant(self,request):
        try:
            get_object_or_404(Plant.objects.all())
            return Response("Nie możesz posadzić nowej rośliny ponieważ jedna już jest posadzona", status=HTTP_409_CONFLICT)
        except: 
            serialzier = PlantCreatingSerializer(data=request.data)
            serialzier.is_valid(raise_exception=True)
            serialzier.save()
            return Response('Roślina zasadzona ;D', status=HTTP_201_CREATED)
    
    @action(detail=False, methods=['put'])
    def edit_plant(self, request):
        serializer = PlantEditingSerializer(instance=Plant.objects.get(id=1),data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Roślina przesadzona', status=HTTP_200_OK)
        
        
    @action(detail=False, methods=['get'])
    def get_info(self, request):
        try:
            get_object_or_404(Plant, id=1)
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            serializer = TemperatureandHumidityWaterLevelSerializer(instance=Plant.objects.get(id=1), data={'temperature':temperature, 'air_humidity':humidity, 'water_level':check_water_level()})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(self.serializer_class(Plant.objects.get(id=1)).data, status=HTTP_200_OK)
        except:
            return Response('Najpierw trzeba stworzyć doniczkę', status=HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])
    def water_the_plants(self, request):
        led = LED(18)
        led.on()
        led.off()
        sleep(15)
        return Response('Podlane !')
    
    @action(detail=False, methods=['get'])
    def get_date(self, request):
        return Response(LastWateringSerializer(Plant.objects.get(id=1)).data, status=HTTP_200_OK)
    
    @action(detail=False, methods=['put'])
    def update_date(self, request):
        serializer = LastWateringSerializer(instance=Plant.objects.get(id=1), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Data Updated', status=HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def get_type(self, request):
        return Response(GetFlowerTypeSerializer(Plant.objects.get(id=1)).data, status=HTTP_200_OK)