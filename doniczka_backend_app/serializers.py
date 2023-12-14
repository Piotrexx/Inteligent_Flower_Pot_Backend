from rest_framework import serializers
from .models import Plant

class PlantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class TemperatureandHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('temperature','air_humidity')