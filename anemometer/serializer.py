from django.urls import path, include
from django.contrib.auth.models import User
from anemometer.models import modeloAnemometer
from rest_framework import serializers

# Serializers define the API representation.
class AnemometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloAnemometer
        fields = '__all__'
        
