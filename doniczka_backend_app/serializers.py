from rest_framework import serializers
from .models import Plant

class PlantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'