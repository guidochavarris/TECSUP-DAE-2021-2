from django.db import models
from django.db.models.base import Model

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion

class Asistencia(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.RESTRICT)
    alumno = models.CharField(max_length=200,null=True)
    fechainicio = models.DateTimeField(auto_now=True)
    fechafin = models.DateTimeField(null=True)

    def __str__(self):
        return self.alumno

