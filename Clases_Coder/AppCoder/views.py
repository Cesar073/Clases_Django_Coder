from django.shortcuts import render
from .models import Curso
from AppCoder.forms import CursoFormulario, BuscaCursoForm

def inicio(request):
    return render(request, "AppCoder/index.html")


def cursos_create_comun_form(request):

    if request.method == 'POST':

        curso =  Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "AppCoder/index.html")

    return render(request,"AppCoder/create_form_comun.html")


def cursos_create_api_form(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])

            curso.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/create_api_form.html", {"miFormulario": miFormulario})


def cursos_read_api_form(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/show_courses.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppCoder/read_api_form.html", {"miFormulario": miFormulario})

