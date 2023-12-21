from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Plant
from .serializers import PlantModelSerializer,PlantCreatingSerializer, TemperatureandHumiditySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST,HTTP_409_CONFLICT, HTTP_201_CREATED
import Adafruit_DHT
from gpiozero import LED
from time import sleep

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

    # @action(detail=False, methods=['put'])
    # def update_temp(self, request):
    #     humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
    #     serializer = TemperatureandHumiditySerializer(data={'temperature':temperature, 'air_humidity':humidity})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('Temperatura zaktualizowana')
    
    @action(detail=False, methods=['put'])
    def edit_plant(self, request):
        try:
            serializer = PlantCreatingSerializer(instance=Plant.objects.get(id=1),data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('Roślina przesadzona', status=HTTP_200_OK)
        except:
            return Response('Aby roślinę przesadzić trzeba ja najpierw zasadzić', status=HTTP_409_CONFLICT)
        
    @action(detail=True, methods=['get'])
    def get_info(self, request, pk):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        serializer = TemperatureandHumiditySerializer(instance=Plant.objects.get(id=pk), data={'temperature':temperature, 'air_humidity':humidity})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(self.serializer_class(Plant.objects.get(id=pk)).data, status=HTTP_200_OK)
        
    @action(detail=False, methods=['get'])
    def water_the_plants(self, request):
        led = LED(18)
        led.on()
        led.off()
        sleep(15)
        return Response('Podlane !')
    