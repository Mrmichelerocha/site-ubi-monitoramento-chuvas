from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('dataanem', AnemometerViewSet, basename='dataanem')

urlpatterns = [
    path('', include(router.urls)),
    path('anemometer', views.anemometerall, name="anemometer"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

