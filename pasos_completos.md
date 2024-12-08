# CLASES DE DJANGO EN CODERHOUSE

## CLASE 6: Clase 22 - Playground Avanzado Parte I
---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`
2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.
3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_22-Playground_Avanzado_Parte_I`

---
## CRUD con funciones
CRUD es el acrónimo de *Create*, *Read*, *Update* y *Delete*, que significan Crear, Leer, Actualizar y Eliminar haciendo referencia a acciones aplicadas sobre la base de datos.<br>
A continuación se va a explicar cómo hacer un CRUD paso a paso en vistas basadas en funciones que son el tipo de vistas que estuvimos programando hasta el momento. En los ejemplos que se van a detallar, no se mostrarán los archivos con el contenido completo sino los cambios o agregados necesarios para llegar al resultado esperado y sólo vamos a realizar el CRUD completo para el modelo llamado "Curso", pero las acciones deberian replicarse en todos los modelos que lo requieran.<br>
Por último, entendemos que continuamos desde lo que dejamos la clase anterior donde ya hicimos la parte de *Create* usando formularios.<br>
Damos por hecho que tenemos en nuestro proyecto el archivo **forms.py**:
```python
from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()
```
### Create (Crear)
1. Para crear nuevos registros en la base de datos, seguimos los pasos de la clase anterior donde nos habíamos apoyado en el uso de formularios.<br>
Agregar el path para la vista donde colocaremos la lógica asociada a la creación de un nuevo registro de la tabla Curso.<br>
Archivo **urls.py**:
    ```python
    from AppCoder import views

    urlpatterns = [
        path('crear_cursos/', views.crear_cursos, name="CrearCursos"),
    ]
    ```
2. Creamos la vista que toma dos decisiones, si el método fue GET sólo muestra el formulario vacío para ser rellenado por el usuario y si el método fue POST obtenemos del request los datos del formulario y los utilizamos para crear un nuevo registro.<br>
Archivo **views.py**:
    ```python
    from django.shortcuts import render
    from .models import Curso
    from AppCoder.forms import CursoFormulario, BuscaCursoForm

    def crear_cursos(request):

        if request.method == "POST":
            miFormulario = CursoFormulario(request.POST)
            
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()
                return render(request, "AppCoder/index.html")
        else:
            miFormulario = CursoFormulario()

    return render(request, "AppCoder/form_con_api.html", {"miFormulario": miFormulario})
    ```
3. Vamos a preparar el template para recibir y mostrar el formulario creado en **forms.py**.<br>
    Nuestro html quedaría así:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Crear Cursos {% endblock title %}

    {% block main %}
    
        <form action="" method="POST">
            {% csrf_token %}
            <table>
                {{ miFormulario.as_table }}
            </table>
            <input type="submit" value="Enviar">

        </form>
    {% endblock main %}

    ```

---
### Read (Leer)
1. Para leer todos los registros de la base de datos y mostrarlos en pantalla, comenzaremos por crear el path correspondiente.<br>
Archivo **urls.py**:
    ```python
    from AppCoder import views

    urlpatterns = [
        path('crear_cursos/', views.crear_cursos, name="CrearCursos"),
        path('ver_cursos/', views.ver_cursos, name="VerCursos"),
    ]
    ```
2. Creamos la vista que obtiene todos los cursos que hayan en la base de datos y se lo enviamos al template.<br>
Archivo **views.py**:
    ```python
    from django.shortcuts import render
    from .models import Curso
    from AppCoder.forms import CursoFormulario, BuscaCursoForm

    def crear_cursos(request):

        if request.method == "POST":
            miFormulario = CursoFormulario(request.POST)
            
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()
                return render(request, "AppCoder/index.html")
        else:
            miFormulario = CursoFormulario()

    return render(request, "AppCoder/form_con_api.html", {"miFormulario": miFormulario})
    ```
3. Luego, vamos a ubicar las partes donde consideramos que cambiarían en cada página y la encerramos entre el juego de llaves y porcentajes: {% %}.<br>
    Por ejemplo, si queremos que el título de la pestaña cambie en función a la página que se visita, podemos escribir lo siguiente:<br>
    `{% block title %} Index {% endblock title %}`<br>
    De ésta forma, cada página que hereda del html base podrá ingresar su propio título o bien, si no colocamos nada en la página que hereda quedará por defecto "Index".<br>
    Nuestro html quedaría así:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Crear Cursos {% endblock title %}

    {% block main %}
    
        <form action="" method="POST">
            {% csrf_token %}
            <table>
                {{ miFormulario.as_table }}
            </table>
            <input type="submit" value="Enviar">

        </form>
    {% endblock main %}

    ```




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
