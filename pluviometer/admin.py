from django.contrib import admin
from pluviometer.models import modeloPluviometer

# Register your models here.
class pluviometer(admin.ModelAdmin):
    pass
admin.site.register(modeloPluviometer, pluviometer)