from django.shortcuts import render
from Escuela.models import *
from Escuela.forms import *

def Inicio(request):
    return render(request, 'Escuela/inicio.html')

def buscar_profesores(request):
    return render(request, "Escuela/profesores.html")

def resultado_buscar_profesores(request):
    nombre_profesor=request.GET["nombre_profesor"]
    profesores=Profesor.objects.filter(nombre__icontains=nombre_profesor)
    return render(request, "Escuela/resultado_buscar_profesor.html", {"profesores":profesores})

def buscar_alumnos(request):
    return render(request, "Escuela/alumnos.html")

def resultado_buscar_alumnos(request):
    nombre_alumno=request.GET["nombre_alumno"]
    alumnos=Alumno.objects.filter(nombre__icontains=nombre_alumno)
    return render(request, "Escuela/resultado_buscar_alumno.html", {"alumnos":alumnos})

def buscar_notas(request):
    return render(request, "Escuela/notas.html")

def resultado_buscar_notas(request):
    nombre_nota=request.GET["nombre_notas"]
    notas=Notas.objects.filter(alumno__icontains=nombre_nota)
    return render(request, "Escuela/resultado_buscar_notas.html", {"notas":notas})

def contacto(request):
    return render(request, "Escuela/contacto.html")

def inicio_profesores(request):
    return render(request, "Escuela/profesores-inicio.html")

def inicio_alumnos(request):
    return render(request, "Escuela/alumnos-inicio.html")

def inicio_notas(request):
    return render(request, "Escuela/notas-inicio.html")

def crear_profesores(request):
    if request.method =="POST":
        formulario = CrearProfesores(request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            profesor= Profesor(nombre=data["nombre"], apellido=data['apellido'],materia=data["materia"])
            profesor.save()
    else:
        formulario = CrearProfesores()
    contexto = {"formulario": formulario}
    return render(request, "Escuela/profesores-crear.html", contexto)

def crear_alumnos(request):
    if request.method =="POST":
        formulario = CrearAlumnos(request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            alumno= Alumno(nombre=data["nombre"], apellido=data['apellido'],curso=data["curso"])
            alumno.save()
    else:
        formulario = CrearAlumnos()
    contexto = {"formulario": formulario}
    return render(request, "Escuela/profesores-crear.html", contexto)

def crear_notas(request):
    if request.method =="POST":
        formulario = CrearNotas(request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            nota= Notas(alumno=data["alumno"], materia=data['materia'],nota=data["nota"])
            nota.save()
    else:
        formulario = CrearNotas()
    contexto = {"formulario": formulario}
    return render(request, "Escuela/profesores-crear.html", contexto)