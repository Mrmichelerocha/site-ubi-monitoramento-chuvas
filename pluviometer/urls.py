from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('datapluv', PluviometerViewSet, basename='datapluv')

urlpatterns = [
    path('', include(router.urls)),
    path('pluviometer', views.pluviometerall, name="pluviometer"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

