from django.shortcuts import render
from .models import Estudiante, Administrador

def home(request):
    return render(request, 'pagina_web/home.html')  # ← Ruta completa

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'pagina_web/estudiantes.html', {'estudiantes': estudiantes})

def lista_administradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'pagina_web/administradores.html', {'administradores': administradores})

def acerca_de(request):
    return render(request, 'pagina_web/acerca_de.html')