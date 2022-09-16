from django.db import models

from .malfunction import Malfunction


class CarMalfunction(models.Model):
    type = models.ManyToManyField(Malfunction, help_text='Введите область поломки')
