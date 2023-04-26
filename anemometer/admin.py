from django.contrib import admin
from anemometer.models import modeloAnemometer

# Register your models here.
class anemometer(admin.ModelAdmin):
    pass
admin.site.register(modeloAnemometer, anemometer)