from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Plant
from .serializers import PlantModelSerializer,PlantCreatingSerializer, TemperatureandHumiditySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import Adafruit_DHT

class PlantViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Plant.objects.all()
    serializer_class = PlantModelSerializer
    sensor = Adafruit_DHT.DHT11
    pin = 4

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
    
    @action(detail=False, methods=['get'])
    def get_info(self,request):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        serializer = TemperatureandHumiditySerializer(data={'temperature':temperature, 'air_humidity':humidity})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(self.serializer_class(Plant.objects.all()).data)