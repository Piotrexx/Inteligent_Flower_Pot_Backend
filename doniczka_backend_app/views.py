from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import AllowAny
from .models import Plant
from .serializers import PlantModelSerializer


class PlantViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Plant.objects.all()
    serializer_class = PlantModelSerializer