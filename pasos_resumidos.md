### Git
1. `git checkout main`
2. `git pull`
3. `git checkout -b clase_18-Portofio_Parte_II`
---

### Django: Templates

#### Agregamos diccionarios
1. 
```python
def probando_template(request):

    nombre = "Adrian"
    apellido = "Holovaty"
    diccionario = {"nombre": nombre, "apellido": apellido}

    # Abrimos el archivo html
    mi_html = open('./Clases_Coder/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto con los datos del diccionario
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
```
2.
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p style="color: red"> Hola {{nombre}}, estamos haciendo uso de variables por contexto</p>
    <p style="color: green">Y podemos acceder al apellido "{{apellido}}" porque tenemos acceso a ambas variables.<br>
    También aplicamos estilos pero luego lo haremos con CSS porque no es buena práctica hacerlo en el archivo html.</p>
</body>
</html>
```
#### Enviamos una lista y recorremos con bucle
1. `diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}`
2.
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <p style="color: red"> Hola {{nombre}}, estamos haciendo uso de variables por contexto</p>
        <p style="color: green">Y podemos acceder al apellido "{{apellido}}" porque tenemos acceso a ambas variables.<br>
        También aplicamos estilos pero luego lo haremos con CSS porque no es buena práctica hacerlo en el archivo html.</p>
        <h2>Notas:</h2>
        {% for n in notas %}
            <p>Nota: {{n}}</p>
        {% endfor %}
    </body>
</html>
```
#### Agregamos conidicional
1. 
```html
        {% for n in notas %}
            {% if n <= 4 %}
                <p style="color: red">Reprobado: {{n}}</p>
            {% else %}
                <p style="color: green">Aprobado: {{n}}</p>
            {% endif %}
        {% endfor %}
```
#### Agregamos loader (cargadores)
1. **views.py**: `from django.template import loader`
2. 
```python
def usando_loader(request):
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
```
3. **DIRS**:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./Clases_Coder/plantillas/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
4. Actualizamos el path.
    ```python
    from django.contrib import admin
    from django.urls import path
    from .views import (
        saludo,
        muestra_nombre,
        probando_template,
        usando_loader
    )

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludo/', saludo),
        path('muestra_nombre/<nombre>/', muestra_nombre),
        path('probando_template/', probando_template),
        path('usando_loader/', usando_loader),
    ]
    ```
---

### Django: Modelos y Aplicaciones
1. Creamos una app:<br>
    `python manage.py startapp AppCoder`
2. Actualizamos **settings.py**:
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'AppCoder',
    ]
    ```
3. Creamos los **models.py**:
```python
from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    apellido = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
```
4. Corremos migraciones:<br>
    `python manage.py makemigrations`<br>
    `python manage.py migrate`
---
### Django: Agregando información a la base de datos
1. 
```python
from AppCoder.models import Curso

def curso(request, nombre, numero):
    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save()
    documento = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
    return HttpResponse(documento)
```
2. Agregamos el path nuevo importando previamente la función:
    ```python
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
    ```
---

### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Paso 1 del proyecto: 1er clase"`
    * `git push --set-upstream origin clase_18-Portfolio_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
