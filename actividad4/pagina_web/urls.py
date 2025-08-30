
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estudiantes/', views.lista_estudiantes, name='estudiantes'),
    path('administradores/', views.lista_administradores, name='administradores'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
]