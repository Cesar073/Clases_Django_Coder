from django.shortcuts import render
from .models import Curso
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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
