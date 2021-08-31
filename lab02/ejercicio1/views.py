

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "calculadora",
    }
    return render(request, 'ejercicio1/dato.html', context)

def enviar(request):

    numero1 = int(request.POST['numero1'])
    numero2 = int(request.POST['numero2'])
    operacion = request.POST['operacion']
    resultado = 0

    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'multiplicacion':
        resultado = numero1 * numero2

    context = {
        'titulo' : "Resultado",
        'numero1' : numero1,
        'numero2' : numero2,
        'operacion' : operacion,
        'resultado' : resultado,
    }

    return render(request, 'ejercicio1/result.html', context)