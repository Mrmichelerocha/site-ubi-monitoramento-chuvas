from django.db import models
# Create your models here.

class modeloUmidity(models.Model):
    status = models.FloatField()
    data = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)