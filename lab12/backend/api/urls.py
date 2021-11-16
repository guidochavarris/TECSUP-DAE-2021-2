
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cursos',views.cursos),
    path('asistencia',views.asistencia),
    path('asistencia/<int:asistencia_id>',views.asistenciadetalle)
]
