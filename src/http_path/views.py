from django.shortcuts import get_object_or_404, Http404
from django.http.response import FileResponse
from http_path.models import Temp, HumidityURL, PluviometerURL, AnemometerURL, LoraIp
from http_path.serializer import TempSerializer, HumidityURLSerializer, PluviometerURLSerializer, AnemometerURLSerializer, LoraIpSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import json
    
class TempURLViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer
    
class HumidityURLViewSet(viewsets.ModelViewSet):
    queryset = HumidityURL.objects.all()
    serializer_class = HumidityURLSerializer
    
class PluviometerURLViewSet(viewsets.ModelViewSet):
    queryset = PluviometerURL.objects.all()
    serializer_class = PluviometerURLSerializer
    
class AnemometerURLViewSet(viewsets.ModelViewSet):
    queryset = AnemometerURL.objects.all()
    serializer_class = AnemometerURLSerializer
    
class LoraIpViewSet(viewsets.ModelViewSet):
    queryset = LoraIp.objects.all()
    serializer_class = LoraIpSerializer
    def post(self, request, format=None):
        serializer = LoraIpSerializer(data=request.data)
        if serializer.is_valid():
            # Faça algo com o dado validado, por exemplo, salve no banco de dados
            dado = serializer.validated_data['dado']
            # Realize qualquer ação adicional necessária
            # ...
            return Response({'success': True})
        else:
            return Response(serializer.errors, status=400)