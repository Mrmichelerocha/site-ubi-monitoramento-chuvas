from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('datatemp', TempURLViewSet, basename='datatemp')
router.register('dataumi', HumidityURLViewSet, basename='dataumi')
router.register('dataane', AnemometerURLViewSet, basename='dataane')
router.register('datapluv', PluviometerURLViewSet, basename='datapluv')
router.register('loraip', LoraIpViewSet, basename='loraip')

urlpatterns = [
    path('routers', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]