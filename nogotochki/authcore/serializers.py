from django.forms import CharField
from rest_framework import generics, serializers

from .models import User, Service


class EmailSerializer(serializers.ModelSerializer):
    email = CharField(required=True)
    password = CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password']


class SignUpSerializer(serializers.ModelSerializer):
    fio = CharField(required=True)
    email = CharField(required=True)
    password = CharField(required=True)

    class Meta:
        model = User
        fields = ['fio', 'email', 'password']


class ServiceSerializer(serializers.ModelSerializer):
    name = CharField(required=True)
    description = CharField(required=True)
    price = CharField(required=True)

    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'price']
