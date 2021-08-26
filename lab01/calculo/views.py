from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("por favor calcule los numeros que desee :) como suma ,resta,multiplicar ,dividir")


def suma(request, pregunta_id, pregunta_id2):
    response = "El resultado de la suma es  %s."
    return HttpResponse(response % int(pregunta_id+pregunta_id2))

def resta(request, pregunta_id, pregunta_id2):
    response = "El resultado de la resta es  %s."
    return HttpResponse(response % int(pregunta_id-pregunta_id2))

def multiplicacion(request, pregunta_id, pregunta_id2):
    response = "El resultado de la multiplicacion es  %s."
    return HttpResponse(response % int(pregunta_id*pregunta_id2))

def division(request, pregunta_id, pregunta_id2):
    response = "El resultado de la division es  %s."
    return HttpResponse(response % int(pregunta_id/pregunta_id2))

# Create your views here.
# Create your views here.
