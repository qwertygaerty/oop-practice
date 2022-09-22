from django.forms import CharField
from rest_framework import generics, serializers

from .models import User


class EmailSerializer(serializers.ModelSerializer):
    email = CharField(required=True)
    password = CharField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password']
