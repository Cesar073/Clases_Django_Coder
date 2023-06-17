from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/class_list.html"

    def get(self, *args, **kwargs):
        print("\n\nEJECUTANDO GET\n\n")
        return super().get(*args, **kwargs)


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppCoder/class_detail.html"

    # login_url = '/users/login/'

    # def get_login_url(self):
    #     return self.login_url


class CursoCreateView(CreateView):
    """
    Esta clase envía por defecto un formulario al archivo html. Envía los campos indicados en la lista "fields" y podemos hacer uso de dicho formulario bajo la key "form".
    """

    model = Curso
    template_name = "AppCoder/class_create.html"
    fields = ["nombre", "camada"]

    # En success_url indicamos la vista que queremos visitar una vez que se genera un curso con éxito. Lo podemos hacer de 2 formas:
    
    # Indicando la URL
    # success_url = "/class-list/"
    # Con el reverse_lazy indicamos el nombre de la vista
    success_url = reverse_lazy("Profesores")


class CursoUpdateView(UpdateView):
    model = Curso
    success_url = reverse_lazy("List")
    fields = ["id", "nombre", "camada"]
    template_name = "AppCoder/class_update.html"


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("List")
    template_name = 'AppCoder/class_confirm_delete.html'

