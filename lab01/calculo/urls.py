from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('sumar/<int:pregunta_id>/<int:pregunta_id2>/', views.suma, name='sumar'),
    
    path('restar/<int:pregunta_id>/<int:pregunta_id2>/', views.resta, name='restar'),
    
    path('multiplicar/<int:pregunta_id>/<int:pregunta_id2>/', views.multiplicacion, name='multiplicar'),

    path('dividir/<int:pregunta_id>/<int:pregunta_id2>/', views.division, name='dividir'),
    
]
