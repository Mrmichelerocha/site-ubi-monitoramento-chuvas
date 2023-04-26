from django.contrib import admin
from umidity.models import modeloUmidity

# Register your models here.
class umidity(admin.ModelAdmin):
    pass
admin.site.register(modeloUmidity, umidity)