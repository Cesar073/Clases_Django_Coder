# CLASES DE DJANGO EN CODERHOUSE

## CLASE 4: Clase 20 - Playground intermedio Parte II
---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. `git checkout main`
2. `git pull`
3. `git checkout -b clase_20-Playground_intermedio_Parte_II`

---
### Herencia de Templates
1. Crear el archivo base:
    ```html
    <!DOCTYPE html>
        <html lang="es">
        <head>
            {% load static %}
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
            <meta name="description" content="" />
            <meta name="author" content="" />
            <title>{% block title %} Index {% endblock title %}</title>
            <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
            <!-- Font Awesome icons (free version)-->
            <script src="https://use.fontawesome.com/releases/v6.3.0/js/all.js" crossorigin="anonymous"></script>
            <!-- Core theme CSS (includes Bootstrap)-->
            <link href="{% static 'AppCoder/css/styles.css' %}" rel="stylesheet" />
        </head>
        <body id="page-top">
            <!-- Navigation-->
            <nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
                <div class="container px-5">
                    <a class="navbar-brand" href="#page-top">Start Bootstrap</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navbarResponsive">
                        <ul class="navbar-nav ms-auto">
                            <li class="nav-item"><a class="nav-link" href="#!">Iniciar sesión</a></li>
                            <li class="nav-item"><a class="nav-link" href="#!">Crear cuenta</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            {% block main %}
            {% endblock main %}
            <!-- Footer-->
            <footer class="py-5 bg-black">
                <div class="container px-5"><p class="m-0 text-center text-white small">Copyright &copy; Your Website 2023</p></div>
            </footer>
        </body>
    </html>
    ```
2. Creamos todos los html que heredan de ese archivo base:
    - Indicar que vamos a heredear del otro archivo: `{% extends 'AppCoder/base.html' %}`
    - También cargamos los estáticos: `{% load static %}`
    - Y creamos el bloque que queremos incrustar: `{% block title %} Template hecho con Herencia {% endblock title %}`
    
    ```html
    {% extends 'AppCoder/base.html' %}
    
    {% load static %}

    {% block title %} Template hecho con Herencia {% endblock title %}

    {% block main %}
    <h1>Este es el título del Inicio que cambio</h1>
    <p>Se ha heredado todo desde la plantilla padre</p>
    <h3>En el hijo, inicio.html, casí no hay nada :)</h3>
    {% endblock main %}
    ```

---
### Navegando entre templates
1. Vamos a indicar en nuestro **urls.py** un nombre para cada url:
    ```python
    urlpatterns = [
        path('/', views.inicio, name="Inicio"),
        path('profesores/', views.profesores, name="Profesores"),
        path('estudiantes/', views.estudiantes, name="Estudiantes"),
        path('cursos/', views.cursos, name="Cursos"),
        path('entregables/', views.entregables, name="Entregables")
    ]
    ```
2. Llamados a nuestros links:
    ```html
    <nav class="navbar navbar-light bg-light static-top">
        <div class="container">
            <a class="navbar-brand" href="{% url 'Inicio' %}">Inicio</a>
            <a class="navbar-brand" href="{% url 'Profesores' %}">Profesores</a>
            <a class="navbar-brand" href="{% url 'Estudiantes' %}">Estudiantes</a>
            <a class="navbar-brand" href="{% url 'Cursos' %}">Cursos</a>
            <a class="navbar-brand" href="{% url 'Entregables' %}">Entregables</a>
            <a class="btn btn-primary" href="#NADAAUN">INICIAR</a>
        </div>
    </nav>
    ```
3. **views.py**:
    ```python
    from django.shortcuts import render

    def inicio(request):
        return render(request, "AppCoder/index.html")
    ```

---
### Panel Admin de Django
1. **admin.py**:
    ```python
    from django.contrib import admin
    from .models import Profesor, Estudiante, Curso, Entregable

    admin.site.register(Profesor)
    admin.site.register(Estudiante)
    admin.site.register(Curso)
    admin.site.register(Entregable)
    ```
2. Consola de Django:
    - `python manage.py createsuperuser`
    - Cargamos un user
    - Cargamos un mail
    - Cargamos el password y lo repetimos

3. Ya podemos ingresar a nuestro panel de Admin.

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos Herencia e iniciamos el Admin de Django"`
    * `git push --set-upstream origin clase_20-Playground_intermedio_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
