import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

MAX_TEMPERATURE_SIZE = 50


class Location(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=4)
    lon = models.DecimalField(max_digits=8, decimal_places=4)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)


class Weather(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(default=datetime.date.today, blank=True, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    temperature = ArrayField(
        models.DecimalField(max_digits=8, decimal_places=4),
        size=MAX_TEMPERATURE_SIZE
    )
