from django.db import models
from rest_framework.authentication import get_authorization_header


class Role(models.Model):
    name = models.CharField(max_length=100, blank=False)
    code = models.CharField(max_length=50, blank=False, unique=True)

    class Meta:
        db_table = 'roles'


class User(models.Model):
    fio = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default='client', to_field='code', unique=False)

    @classmethod
    def get_auth_user(cls, request=None):
        keyword = 'Bearer'
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != keyword.lower().encode() or not auth[1]:
            return None
        return cls.objects.filter(api_token=auth[1].decode()).first()

    class Meta:
        db_table = 'users'


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)


class Cart(models.Model):
    items = models.ManyToManyField(Service, related_name='services')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    @classmethod
    def get_services(cls):
        return cls.items

