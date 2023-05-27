from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")