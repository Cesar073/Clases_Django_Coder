from django.http import HttpResponse

# Create your views here.
from AppCoder.models import Curso

def curso(request, nombre, numero):
    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save()
    
    documento = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
    return HttpResponse(documento)