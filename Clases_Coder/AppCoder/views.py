from django.shortcuts import render
from .models import Curso
from AppCoder.forms import CursoFormulario, BuscaCursoForm
from django.contrib.auth.decorators import login_required
from users.models import Avatar

def inicio(request):
    
    try:
        url = Avatar.objects.filter(user=request.user.id)[0].imagen.url
    except IndexError:
        url = None

    return render(request, "AppCoder/index.html", {"url": url})

@login_required
def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")

def form_comun(request):

    if request.method == 'POST':

        curso =  Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "AppCoder/index.html")

    return render(request,"AppCoder/form_comun.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])

            curso.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppCoder/buscar_form_con_api.html", {"miFormulario": miFormulario})

def mostrar_cursos(request):

    cursos = Curso.objects.all() #trae todos los profesores

    contexto= {"cursos":cursos} 

    return render(request, "AppCoder/mostrar_cursos.html",contexto)

def clase_22_cursos(request, id):

    profesor = Curso.objects.get(id=id)
    profesor.delete()
 
    # vuelvo al menú
    cursos = Curso.objects.all()  # trae todos los profesores
 
    contexto = {"cursos": cursos}
 
    return render(request, "AppCoder/mostrar_cursos.html", contexto)

