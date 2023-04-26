from django.shortcuts import render
from pluviometer.serializer import PluviometerSerializer
from pluviometer.models import modeloPluviometer
from rest_framework import viewsets

# Create your views here.
class PluviometerViewSet(viewsets.ModelViewSet):
    queryset = modeloPluviometer.objects.all()
    serializer_class = PluviometerSerializer
    
def pluviometerall(request):
    data = {}
    data['db'] = modeloPluviometer.objects.all()
    return render(request, 'temperature.html', data)