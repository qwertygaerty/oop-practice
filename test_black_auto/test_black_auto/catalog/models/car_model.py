from django.db import models

from .car_brand import Brand


class CarModel(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='uploads/cars/')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
