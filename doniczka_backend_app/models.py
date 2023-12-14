from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    plant_specie = models.CharField(max_length=100)
    ground_humidity = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
    air_humidity = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
    water_level = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(100)])
    temperature = models.FloatField(default=0,)
