from django.urls import path, include
from django.contrib.auth.models import User
from umidity.models import modeloUmidity
from rest_framework import serializers

# Serializers define the API representation.
class UmiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloUmidity
        fields = '__all__'
        
