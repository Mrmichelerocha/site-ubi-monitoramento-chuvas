from django.shortcuts import render
from umidity.serializer import UmiditySerializer
from umidity.models import modeloUmidity
from rest_framework import viewsets

# Create your views here.
class UmidityViewSet(viewsets.ModelViewSet):
    queryset = modeloUmidity.objects.all()
    serializer_class = UmiditySerializer
    
def umidityall(request):
    data = {}
    data['db'] = modeloUmidity.objects.all()
    return render(request, 'temperature.html', data)