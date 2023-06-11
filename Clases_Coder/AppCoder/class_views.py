from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso
from .forms import CursoFormulario
from django.urls import reverse_lazy

class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/class_list.html"


class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/class_detail.html"


class CursoCreateView(CreateView):
    """
    Esta clase envía por defecto un formulario al archivo html. Envía los campos indicados en la lista "fields" y podemos hacer uso de dicho formulario bajo la key "form".
    """

    model = Curso
    template_name = "AppCoder/class_create.html"
    fields = ["nombre", "camada"]

    # En success_url indicamos la vista que queremos visitar una vez que se genera un curso con éxito. Lo podemos hacer de 2 formas:
    
    # Indicando la URL
    # success_url = "../class-list/"
    # Con el reverse_lazy indicamos el nombre de la vista
    success_url = reverse_lazy("List")


class CursoUpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy("List")
    fields = ["nombre", "camada"]
    template_name = "AppCoder/class_update.html"


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("List")
    template_name = 'AppCoder/class_confirm_delete.html'

