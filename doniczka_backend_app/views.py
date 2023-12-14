from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Plant
from .serializers import PlantModelSerializer,PlantCreatingSerializer, TemperatureandHumiditySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PlantViewSet(GenericViewSet):
    permission_classes = [AllowAny]
    queryset = Plant.objects.all()
    serializer_class = PlantModelSerializer

    @action(detail=False, methods=['post'])
    def create_plant(self,request):
        serialzier = PlantCreatingSerializer(data=request.data)
        serialzier.is_valid(raise_exception=True)
        serialzier.save()
        return Response('Roślina zasadzona ;D')

    @action(detail=False, methods=['put'])
    def update_temp(self, request):
        serializer = TemperatureandHumiditySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Temperatura zaktualizowana')
    
    @action(detail=False, methods=['get'])
    def get_info(self,request):
        return Response(self.serializer_class(Plant.objects.all()).data)