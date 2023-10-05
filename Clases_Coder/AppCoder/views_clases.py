from django.shortcuts import render
from .models import Curso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        print(form)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            nombre_usuario = authenticate(username=usuario, password=clave)

            if usuario is not None:
                login (request, nombre_usuario)
                return render(request, "AppCoder/index.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "AppCoder/login.html", {"mensaje":"Error, datos incorrectos", "form": form})
        else:
            return render(request, "AppCoder/index.html", {"mensaje":"Error, formulario inválido"})
    
    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form":form})


class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_list.html"


class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_detalle.html"


class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_form.html"
    success_url = reverse_lazy("List")
    fields = ["nombre", "camada"]


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppCoder/Vistas_Clases/curso_edit.html"
    #success_url = reverse_lazy("List")
    success_url = "/AppCoder/clases/lista/"
    fields = ["nombre", "camada"]


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("List")
    template_name = "AppCoder/Vistas_Clases/curso_confirm_delete.html"

