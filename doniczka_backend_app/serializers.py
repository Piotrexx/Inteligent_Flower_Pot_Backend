from rest_framework import serializers
from .models import Plant

class PlantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class TemperatureandHumidityWaterLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('temperature','air_humidity', 'water_level')

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

class LastWateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('last_watering',)

class GetFlowerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('plant_specie',)


class SaveGroundHumidity(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('ground_humidity',)