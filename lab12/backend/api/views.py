#from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Curso,Asistencia
from .serializers import CursoSerializer,AsistenciaSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'mensaje':'Api rest de asistencia'})


@api_view(['GET'])
def cursos(request):
    listCursos = Curso.objects.all()
    serCursos = CursoSerializer(listCursos,many=True)
    return Response(serCursos.data)    

@api_view(['GET','POST'])
def asistencia(request):
    if request.method == 'GET':
            listAsistencia = Asistencia.objects.all()
            serAsistencia = AsistenciaSerializer(listAsistencia,many=True)
            return Response(serAsistencia.data)  
    elif request.method == 'POST':
        serAsistencia = AsistenciaSerializer(data=request.data)
        if serAsistencia.is_valid():
            serAsistencia.save()
            return Response(serAsistencia.data)
        else:
            return Response(serAsistencia.errors)              

@api_view(['GET','PUT','DELETE'])
def asistenciadetalle(request,asistencia_id):
    objAsistencia = Asistencia.objects.get(id=asistencia_id)

    if request.method == 'GET':
        serAsistencia = AsistenciaSerializer(objAsistencia)
        return Response(serAsistencia.data)
    elif request.method == 'PUT': 
        serAsistencia = AsistenciaSerializer(objAsistencia,data=request.data)
        if serAsistencia.is_valid():
            serAsistencia.save()
            return Response(serAsistencia.data)   

        else:
            return Response(serAsistencia.errors)
    elif request.method == 'DELETE':
        return Response(status=204)            