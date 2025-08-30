# pagina_web/admin.py
from django.contrib import admin
from .models import Estudiante, Administrador

admin.site.register(Estudiante)
admin.site.register(Administrador)