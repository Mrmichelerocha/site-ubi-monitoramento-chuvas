from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers



router = routers.DefaultRouter()
router.register('dataumid', UmidityViewSet, basename='dataumid')

urlpatterns = [
    path('', include(router.urls)),
    path('umidity', views.umidityall, name="umidity"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

