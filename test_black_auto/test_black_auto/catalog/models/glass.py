from django.db import models

from .car_model import CarModel
from .glass_type import GlassType


class Glass(models.Model):
    # glass_id = models.AutoField(primary_key=True)
    type = models.ManyToManyField(GlassType, help_text='Введите тип стекла',  related_name="types")
    car_model = models.ManyToManyField(CarModel,  related_name="car_models")
    name = models.CharField(max_length=225, null=True)
    country = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name_plural = "Glass"

    def __str__(self):
        return str(self.type)

    def get_types(self):
        return ",".join([str(p) for p in self.type.all()])

    def get_car_models(self):
        return ",".join([str(p) for p in self.car_model.all()])

