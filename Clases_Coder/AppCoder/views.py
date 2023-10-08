from django.shortcuts import render
from .models import Curso
from AppCoder.forms import CursoFormulario, BuscaCursoForm
from django.contrib.auth.decorators import login_required
from users.models import Avatar
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Profesor, Entregable
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


# Dejamos la vista INICIO basada en funciones y visible para todos
def inicio(request):
    return render(request, "AppCoder/index.html")

def inicio_24(request):
    
    try:
        url = Avatar.objects.filter(user=request.user.id)[0].imagen.url
    except IndexError:
        url = None

    return render(request, "AppCoder/index.html", {"url": url})


# Dejamos una vista basada en funciones que requiere login para mostrar el uso de @login_required
@login_required
def about(request):
    return render(request, "AppCoder/about.html")


# VISTAS BASADAS EN CLASES - CURSOS
class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppCoder/curso_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppCoder/curso_detail.html"

    # login_url = '/users/login/'

    # def get_login_url(self):
    #     return self.login_url


class CursoCreateView(LoginRequiredMixin, CreateView):
    """
    Esta clase envía por defecto un formulario al archivo html. Envía los campos indicados en la lista "fields" y podemos hacer uso de dicho formulario bajo la key "form".
    """

    model = Curso
    template_name = "AppCoder/curso_create.html"
    fields = ["nombre", "camada"]

    # En success_url indicamos la vista que queremos visitar una vez que se genera un curso con éxito. Lo podemos hacer de 2 formas:
    
    # Indicando la URL
    # success_url = "/curso-list/"
    # Con el reverse_lazy indicamos el nombre de la vista
    success_url = reverse_lazy("CursoList")


class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    fields = ["nombre", "camada"]
    template_name = "AppCoder/curso_update.html"


class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = 'AppCoder/curso_confirm_delete.html'


# VISTAS BASADAS EN CLASES - ESTUDIANTES
class EstudianteListView(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "AppCoder/estudiante_list.html"


class EstudianteDetailView(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "AppCoder/estudiante_detail.html"


class EstudianteCreateView(LoginRequiredMixin, CreateView):

    model = Estudiante
    template_name = "AppCoder/estudiante_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("EstudianteList")


class EstudianteUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppCoder/estudiante_update.html"


class EstudianteDeleteView(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = 'AppCoder/estudiante_confirm_delete.html'


# VISTAS BASADAS EN CLASES - PROFESORES
class ProfesorListView(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "AppCoder/profesor_list.html"


class ProfesorDetailView(LoginRequiredMixin, DetailView):
    model = Profesor
    template_name = "AppCoder/profesor_detail.html"


class ProfesorCreateView(LoginRequiredMixin, CreateView):
    model = Profesor
    template_name = "AppCoder/profesor_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("ProfesorList")


class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppCoder/profesor_update.html"


class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    template_name = 'AppCoder/profesor_confirm_delete.html'


# VISTAS BASADAS EN CLASES - ENTREGABLES
class EntregableListView(LoginRequiredMixin, ListView):
    model = Entregable
    template_name = "AppCoder/entregable_list.html"


class EntregableDetailView(LoginRequiredMixin, DetailView):
    model = Entregable
    template_name = "AppCoder/entregable_detail.html"


class EntregableCreateView(LoginRequiredMixin, CreateView):
    model = Entregable
    template_name = "AppCoder/entregable_create.html"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    success_url = reverse_lazy("EntregableList")


class EntregableUpdateView(LoginRequiredMixin, UpdateView):
    model = Entregable
    success_url = reverse_lazy("EntregableList")
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "AppCoder/entregable_update.html"


class EntregableDeleteView(LoginRequiredMixin, DeleteView):
    model = Entregable
    success_url = reverse_lazy("EntregableList")
    template_name = 'AppCoder/entregable_confirm_delete.html'




