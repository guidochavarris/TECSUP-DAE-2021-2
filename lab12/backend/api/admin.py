from django.contrib import admin

# Register your models here.

from .models import Curso,Asistencia

admin.site.register(Curso)
admin.site.register(Asistencia)
