from django.urls import path, include
from django.contrib.auth.models import User
from pluviometer.models import modeloPluviometer
from rest_framework import serializers

# Serializers define the API representation.
class PluviometerSerializer(serializers.ModelSerializer):
    class Meta:
        model = modeloPluviometer
        fields = '__all__'
        
