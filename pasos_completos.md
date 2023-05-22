# CLASES DE DJANGO EN CODERHOUSE

## CLASE 2: Clase 18 - Portfolio Parte II
---

### Entorno virtual
De ahora en más, vamos a interpretar que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`
2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.
3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_18-Portofio_Parte_II`
---

### Django: Templates
Resumen:<br>
Vamos a crear datos propios en el back para mostrarlos en el front haciendo uso de un diccionario como contexto. Este diccionario se procesa para ser renderizado junto con el template (archivo html) y enviado al front.<br>
Cabe aclarar que en el ejemplo sólo vamos a crear un diccionario con datos estáticos (o como decimos en la jerga, valores hardcodeados), pero los mismos pueden ser construídos a partir de cualquier acción que deseemos en nuestras funciones, como obtenerlos desde la base de datos, operaciones internas de nuestro desarrollo, etc.

#### Agregamos diccionarios
1. Agregamos a la vista (**views.py**) un diccionario con datos de nombre y apellido y luego lo agregamos al contexto. El resto del código permanece igual:
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

        # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
        mi_contexto = Context(diccionario)

        # Terminamos de construír el template renderizándolo con su contexto
        documento = plantilla.render(mi_contexto)

        return HttpResponse(documento)
    ```
2. En el archivo html, vamos a hacer uso del contexto pero accedemos al mismo con una sintaxis especial y como si fueran variables. Es decir, si queremos acceder al contenido del apellido, sólo vamos a nombrar la key del diccionario que creamos dentro de 2 llaves:
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
1. Ahora vamos a enviar una lista de datos y mostrarla con un bucle.
    Agregamos al diccionario una key adicional con una lista, quedando el diccionario de la siguiente manera:<br>
    `diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}`
2. Así como para acceder a valores dentro de un template usamos dobles llaves, para ejecutar código debemos usar la sintaxis de llaves y símbolo de porcentaje. A continuación, creamos un bucle for en el template para mostrar la lista de notas:
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
1. Además podemos agregar un condicional if, ejemplo:
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
1. Ahora vamos a simplificar el código para cargar plantillas, ya que ésto puede ser tedioso y laborioso. Primero debemos importar en el archivo **views.py** el método que nos permite hacer esto: `from django.template import loader`
2. Luego, vamos a crear una nueva vista en el mismo archivo así podemos comparar la diferencia con el anterior método.
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
3. Debido a que la forma de indicar el archivo html es diferente para este caso, lo que nos falta hacer es editar la lista **TEMPLATES**, y dentro de su diccionario la key **DIRS** que también contiene una lista. Dicha lista se encuentra en el archivo **settings.py**. En ella, podemos indicar el path de todas las carpetas que tendrán archivos html, para facilitar invocarlos cada vez que lo necesitemos tan sólo colocando el nombre del archivo como lo hicimos en la función del archivo **views.py**.
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
    >NOTA: en producción es recomendable colocar el path entero, pero con el punto (.) nos estamos asegurando que el repositorio va a funcionar en cualquier PC que sea descargado. Dicho punto representa todo el path hasta la carpeta donde se encuentra el archivo **manage.py**.
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
>NOTA: Podemos ver que usando un loader ya no tenemos el problema de los acentos y caracteres especiales.
---

### Django: Modelos y Aplicaciones
Una vez que entendemos lo que es una aplicación, vamos a crearla para luego configurar un modelo de Django.
1. Creamos la app ubicandonos desde la consola donde se encuentra el archivo **manage.py**:<br>
    `python manage.py startapp <nombre_app>`<br>
    Ej: `python manage.py startapp AppCoder`
2. Ahora debemos avisarle a Django que hemos creado una aplicación nueva y para que la tenga mapeada la vamos a agregar a su lista de aplicaciones, en el archivo **settings.py**:
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
3. Con el comando anterior (paso 1), se nos ha creado una carpeta (AppCoder) donde se ubicarán los archivos de la app incluyendo el modelo. En el mismo (**models.py**) vamos a crear las siguientes tablas:
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
4. Django nos provee de un sistema de diagnóstico para saber si la app que venimos creando está correcta, lo ejecutamos de la siguiente manera:<br>
`python manage.py check AppCoder`
5. Ya podemos crear los archivos de migraciones, los que le brindarán las directivas para crear las tablas en la base de datos:<br>
    `python manage.py makemigrations`<br>
    Dicho comando, creará en la carpeta de migraciones un archivo numerado con los comandos para que el ORM genere las tablas.
    >NOTA 1: Se pueden observar las verdaderas directivas SQL que se van a ejcutar con el comando: `python manage.py sqlmigrate AppCoder0001`<br>
    >NOTA 2: También podemos ver la lista de migraciones que Django está reconociendo y nos indica las que fueron realizadas y las que no: `python manage.py showmigrations`
6. Ahora podemos ejecutar esas migraciones, ya que sólo las hemos creado pero no se han ejecutado:<br>
    `python manage.py migrate`
---

### DbBrowser
* En esta parte de la clase, se muestra en acción el programa realizando un CRUD. No lo incluímos en éste archivo.
---

### Django: Shell
Django nos proporciona su propia shell para interactuar con el back, en el curso se muestran los pasos en vivo para agregar un registro en el modelo de **Curso**. A continuación vamos a resumir los comandos sin mucho detalle:
1. Abrimos la shell:<br>
    `python manage.py shell`
2. Importamos la tabla Curso:<br>
    `from AppCoder.models import Curso`
3. Creamos una nueva instancia, un nuevo registro:<br>
    `curso = Curso(nombre="Python", camada=40450)`
4. Guardamos los cambios, ya que sólo se encuentran en RAM:<br>
    `curso.save()`
---
### Django: Agregando información a la base de datos
Desde nuestras vistas podemos agregar información a la base de datos. Por el momento vamos a seguir con el método GET, vamos a crear registros nuevos en la tabla de **Cursos** indicando tanto el nombre de una camada como la comisión.
1. Generamos una nueva vista importando previamente el modelo de Curso:
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
