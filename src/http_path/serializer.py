from django.urls import path, include
from django.contrib.auth.models import User
from http_path.models import Temp, HumidityURL, PluviometerURL, AnemometerURL, LoraIp
from rest_framework import serializers

# Serializers define the API representation.        
class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = '__all__'
        
class HumidityURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityURL
        fields = '__all__'
        
class PluviometerURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = PluviometerURL
        fields = '__all__'
        
class AnemometerURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnemometerURL
        fields = '__all__'
        
class LoraIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoraIp
        fields = '__all__'