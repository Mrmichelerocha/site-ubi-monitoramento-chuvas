from django.db import models

# Create your models here.
class HumidityURL(models.Model):
    slug = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class PluviometerURL(models.Model):
    slug = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class AnemometerURL(models.Model):
    slug = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Temp(models.Model):
    slug = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class LoraIp(models.Model):
    url = models.TextField(max_length=200)