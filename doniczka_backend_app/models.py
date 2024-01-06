from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


class Plant(models.Model):

    PLANT_CHOICES = [
        ("Kaktus", "Kaktus"),
        ("Kawa", "Kawa")
    ]

    plant_name = models.CharField(max_length=255)
    plant_specie = models.CharField(max_length=10, choices=PLANT_CHOICES)
    ground_humidity = models.IntegerField(default=0)
    air_humidity = models.IntegerField(default=0)
    water_level = models.BooleanField(default=False)
    temperature = models.FloatField(default=0)
    last_watering = models.DateTimeField(default="")
