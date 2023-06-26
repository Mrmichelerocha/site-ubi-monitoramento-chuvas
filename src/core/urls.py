from django.urls import path, include
from core.views import download_temporary_file, showFirebaseJS
from . import views
from .views import *
from rest_framework import routers

app_name = "core"
router = routers.DefaultRouter()
router.register('datadatamodel', DataModelViewSet, basename='datadatamodel')
router.register('datadata', DataViewSet, basename='datadata')
router.register('datadevicemodel', DeviceModelViewSet, basename='datadevicemodel')
router.register('datadevicelog', DeviceLogViewSet, basename='datadevicelog')
router.register('datadevice', DeviceViewSet, basename='datadevice')
router.register('datafm', FirmwareViewSet, basename='datafm')
router.register('datalocation', LocationViewSet, basename='datalocation')
router.register('dataurltemp', TempURLViewSet, basename='dataurltemp')

urlpatterns = [
    path('routers', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("download/<slug:uuid>/", download_temporary_file, name="download-temporary-file"),
    path("firebase-messaging-sw.js", showFirebaseJS, name="show-firebase-ja"),
]