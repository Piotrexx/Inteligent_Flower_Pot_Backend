from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    ground_humidity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    air_humidity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    water_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    temperature = models.FloatField()
    