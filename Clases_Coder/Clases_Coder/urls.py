"""
URL configuration for Clases_Coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    saludo,
    muestra_nombre,
    probando_template,
    usando_loader,
    curso
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('muestra_nombre/<nombre>/', muestra_nombre),
    path('probando_template/', probando_template),
    path('usando_loader/', usando_loader),
    path('curso/<nombre>/<numero>/', curso),
]