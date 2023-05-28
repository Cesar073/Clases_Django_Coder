# CLASES DE DJANGO EN CODERHOUSE

## CLASE 4: Clase 20 - Playground intermedio Parte II
---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`
2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.
3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_20-Playground_intermedio_Parte_II`

---
### Herencia de Templates
Al crear muchos archivos html podemos darnos cuenta que hay código que se repiten en todos los archivos como la navbar o el footer. Podemos aplicar **Herencia de templates** para evitar escribirlo más de una vez y centralizar el código, facilitando posibles futuros cambios:
1. Crear un archivo html que nos sirva de base, del que todos van a heredar, donde ahí colocaremos la navbar, footer y todo lo que se repita en nuestro proyecto.
2. Luego, vamos a ubicar las partes donde consideramos que cambiarían en cada página y la encerramos entre el juego de llaves y porcentajes: {% %}.<br>
    Por ejemplo, si queremos que el título de la pestaña cambie en función a la página que se visita, podemos escribir lo siguiente:<br>
    `{% block title %} Index {% endblock title %}`<br>
    De ésta forma, cada página que hereda del html base podrá ingresar su propio título o bien, si no colocamos nada en la página que hereda quedará por defecto "Index".<br>
    Nuestro html de base quedaría así:
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
4. Por último, creamos todos los html que heredan de ese archivo base:
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
Para navegar en nuestro sitio, debemos utilizar una sintaxis diferente dentro de nuestros html.
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
2. En los llamados a nuestros links en el html, debemos indicarlos con nueva sintaxis pero haciendo referencia a los nombres recién creados:
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
3. En caso de que aún estemos usando el método render en las vistas, le cambiamos a todas el `HttpResponse` por:
    ```python
    from django.shortcuts import render

    def inicio(request):
        return render(request, "AppCoder/index.html")
    ```
---
### Panel Admin de Django
El panel de administración de Django es una herramienta versátil y muy útil a la hora de administrar una aplicación. Desde una interfaz gráfica podemos realizar acciones del tipo CRUD en cada una de nuestras tablas y administrar usuarios.<br>
Para poder utilizar nuestro Panel de Django con nuestros modelos debemos seguir los siguientes pasos:
1. Ir a cada archivo **admin.py** de cada aplicación y agregamos cada modelo de la siguiente manera:
    ```python
    from django.contrib import admin
    from .models import Profesor, Estudiante, Curso, Entregable

    admin.site.register(Profesor)
    admin.site.register(Estudiante)
    admin.site.register(Curso)
    admin.site.register(Entregable)

    ```
2. Como no existe aún un usuario en nuestro proyecto, vamos a crear un superuser desde la consola de Django:
    - `python manage.py createsuperuser`
    - Cargamos un user (cesar)
    - Cargamos un mail (a@b.com)
    - Cargamos el password y lo repetimos (pass123)

3. Ya podemos ingresar a nuestro panel de Admin (url: `localhost:8000/admin/`) y luego de ingresar las credenciales recién creadas, podremos trabajar con nuestros modelos.

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos Herencia e iniciamos el Admin de Django"`
    * `git push --set-upstream origin clase_20-Playground_intermedio_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
