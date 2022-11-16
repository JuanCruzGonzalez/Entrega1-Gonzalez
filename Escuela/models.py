from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)

class Notas(models.Model):
    alumno = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    nota = models.IntegerField()
