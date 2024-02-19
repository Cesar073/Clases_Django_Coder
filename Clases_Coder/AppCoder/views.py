from django.shortcuts import render
from .models import Curso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Profesor, Entregable
from django.urls import reverse_lazy



# Dejamos la vista INICIO basada en funciones y visible para todos
def inicio(request):
    return render(request, "AppCoder/index.html")


def about(request):
    return render(request, "AppCoder/about.html")


# VISTAS BASADAS EN CLASES - CURSOS
class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/curso_list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detail.html"

    # AGREGADO!
    # Esta es otra forma para redirigir a un login. Tiene prioridad sobre la configuración del settings.py
    login_url = '/users/login/'

    def get_login_url(self):
        return self.login_url
    # FIN DEL CÓDIGO AGREGADO


class CursoCreateView(CreateView):
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


class CursoUpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    fields = ["nombre", "camada"]
    template_name = "AppCoder/curso_update.html"


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("CursoList")
    template_name = 'AppCoder/curso_confirm_delete.html'


# VISTAS BASADAS EN CLASES - ESTUDIANTES
class EstudianteListView(ListView):
    model = Estudiante
    template_name = "AppCoder/estudiante_list.html"


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "AppCoder/estudiante_detail.html"


class EstudianteCreateView(CreateView):

    model = Estudiante
    template_name = "AppCoder/estudiante_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("EstudianteList")


class EstudianteUpdateView(UpdateView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppCoder/estudiante_update.html"


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("EstudianteList")
    template_name = 'AppCoder/estudiante_confirm_delete.html'


# VISTAS BASADAS EN CLASES - PROFESORES
class ProfesorListView(ListView):
    model = Profesor
    template_name = "AppCoder/profesor_list.html"


class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "AppCoder/profesor_detail.html"


class ProfesorCreateView(CreateView):
    model = Profesor
    template_name = "AppCoder/profesor_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("ProfesorList")


class ProfesorUpdateView(UpdateView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    fields = ["nombre", "apellido", "email"]
    template_name = "AppCoder/profesor_update.html"


class ProfesorDeleteView(DeleteView):
    model = Profesor
    success_url = reverse_lazy("ProfesorList")
    template_name = 'AppCoder/profesor_confirm_delete.html'


# VISTAS BASADAS EN CLASES - ENTREGABLES
class EntregableListView(ListView):
    model = Entregable
    template_name = "AppCoder/entregable_list.html"


class EntregableDetailView(DetailView):
    model = Entregable
    template_name = "AppCoder/entregable_detail.html"


class EntregableCreateView(CreateView):
    model = Entregable
    template_name = "AppCoder/entregable_create.html"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    success_url = reverse_lazy("EntregableList")


class EntregableUpdateView(UpdateView):
    model = Entregable
    success_url = reverse_lazy("EntregableList")
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "AppCoder/entregable_update.html"


class EntregableDeleteView(DeleteView):
    model = Entregable
    success_url = reverse_lazy("EntregableList")
    template_name = 'AppCoder/entregable_confirm_delete.html'
