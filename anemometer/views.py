from django.shortcuts import render
from anemometer.serializer import AnemometerSerializer
from anemometer.models import modeloAnemometer
from rest_framework import viewsets

# Create your views here.
class AnemometerViewSet(viewsets.ModelViewSet):
    queryset = modeloAnemometer.objects.all()
    serializer_class = AnemometerSerializer
    
def anemometerall(request):
    data = {}
    data['db'] = modeloAnemometer.objects.all()
    return render(request, 'temperature.html', data)