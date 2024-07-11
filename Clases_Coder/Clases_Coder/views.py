from django.http import HttpResponse
# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder!")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

def probando_template(request):

    nombre = "Gastón"
    apellido = "Holovaty"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }

    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
