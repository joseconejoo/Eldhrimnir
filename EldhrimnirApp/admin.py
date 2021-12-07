from django.contrib import admin

from .models import carreras, carrera_seccion
# Register your models here.

admin.site.register(carrera_seccion)
admin.site.register(carreras)

