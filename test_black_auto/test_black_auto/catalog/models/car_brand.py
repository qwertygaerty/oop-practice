from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=225)
    logo = models.ImageField(upload_to='uploads/brands/')
