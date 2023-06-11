from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso
from .forms import CursoFormulario

class CursoListView(ListView):
    model = Curso
    template_name = "AppCoder/class_list.html"


class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/class_detail.html"


class CursoCreateView(CreateView):
    model = Curso
    # success_url = "AppCoder/ACA VA MOSTRAR"
    success_url = "AppCoder/ACA VA MOSTRAR"
    fields = ["nombre", "camada"]


class CursoUpdateView(UpdateView):
    model = Curso
    success_url = "AppCoder/ACA VA MOSTRAR"
    fields = ["nombre"]


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = "AppCoder/class_confirm_delete.html"

