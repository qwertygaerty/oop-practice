from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=225)
    logo = models.ImageField(upload_to='uploads/brands/')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
