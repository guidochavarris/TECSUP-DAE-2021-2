  
from django.urls import path
from django.urls.resolvers import URLPattern

from .  import views

app_name = 'ejercicio1'

urlpatterns = [
    path('', views.index,name='index'),
    path('enviar',views.enviar,name='enviar'),
]