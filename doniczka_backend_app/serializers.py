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

class PlantCreatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('plant_name','plant_specie')

class PlantEditingSerializer(serializers.ModelSerializer):
    plant_name = serializers.CharField(required=False)
    plant_specie = serializers.CharField(required=False)
    class Meta:
        model = Plant
        fields = ('plant_name', 'plant_specie')

class GroundHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('ground_humidity',)