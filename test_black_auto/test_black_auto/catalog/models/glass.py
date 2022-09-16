from django.db import models

from .car_model import CarModel
from .glass_type import GlassType


class Glass(models.Model):
    type = models.ManyToManyField(GlassType, help_text='Введите тип стекла')
    car_model = models.ManyToManyField(CarModel)
    name = models.CharField(max_length=225, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.type)
