from django.db import models


class Malfunction(models.Model):
    name = models.CharField(max_length=225)

