
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    carrera = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    departamento = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"