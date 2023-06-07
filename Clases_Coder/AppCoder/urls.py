"""
URL configuration for Clases_Coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entregables/', views.entregables, name="Entregables"),
    path('form-comun/', views.form_comun, name="Form-Comun"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api")
]