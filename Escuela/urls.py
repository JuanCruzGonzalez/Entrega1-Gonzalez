from django.urls import path   
from Escuela.views import *
from Escuela import views

urlpatterns = [
    path('profesores/', buscar_profesores, name='buscar-profesores'),
    path('buscar/profesores/', resultado_buscar_profesores, name='resultado-buscar-profesores'),
    path('inicio/', Inicio, name='escuela-inicio'),
    path('alumnos/', buscar_alumnos, name='buscar-alumnos'),
    path('buscar/alumnos/', resultado_buscar_alumnos, name='resultado-buscar-alumnos'),
    path('notas/', buscar_notas, name='buscar-notas'),
    path('buscar/notas', resultado_buscar_notas, name='resultado-buscar-notas'),
    path('buscar/contacto', contacto, name='contacto'),
    path('inicio/profesores', inicio_profesores, name='inicio-profesores'),
    path('inicio/alumnos', inicio_alumnos, name='inicio-alumnos'),
    path('inicio/notas', inicio_notas, name='inicio-notas'),
    path('crear/profesores', crear_profesores, name='crear-profesores'),
    path('crear/alumnos', crear_alumnos, name='crear-alumnos'),
    path('crear/notas', crear_notas, name='crear-notas'),
]