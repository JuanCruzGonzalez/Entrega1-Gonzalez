from django import forms

class CrearProfesores(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    materia=forms.CharField(max_length=30)

class CrearAlumnos(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    curso=forms.CharField(max_length=30)

class CrearNotas(forms.Form):
    alumno=forms.CharField(max_length=30)
    materia=forms.CharField(max_length=30)
    nota=forms.CharField(max_length=30)
