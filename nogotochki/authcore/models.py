from django.db import models


class User(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
