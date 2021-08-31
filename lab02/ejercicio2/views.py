from django.shortcuts import render
import math
from math import *

# Create your views here.
def index(request):
    context = {
        'titulo' : "VOLUMEN DEL CILINDRO",
    }
    return render(request, 'ejercicio2/valor.html', context)

def volum(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    resultado = pi * math.pow(diametro/2, 2) * altura 
    context = {
        'titulo' : "Volumen de Cilindro",
        'resultado' : resultado,
    }
    return render(request, 'ejercicio2/volum.html', context)