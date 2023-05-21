# CLASES DE DJANGO EN CODERHOUSE

## CLASE 1: Clase 17 - Django - Portfolio Parte I
---

### Entorno virtual.
1. Creamos la carpeta donde trabajaremos en nuestro proyecto de Django.
2. Abrimos VsCode posicionándonos en dicha carpeta.
3. `pip install pipenv`
4. `pipenv --python 3.9.13`
5. `pipenv shell`
---

### Instalaciones
1. Creamos el archivo de **requirements.txt**
    ```
    # Python 3.9.13
    django==4.2
    ```
2. `pipenv install -r requirements.txt`
---

### GitHub
* En este apartado no explicaremos demasiado, sólo vamos a crear el repositorio y obtenemos la url para vincularlo con el repositorio local de Git.
---

### Git
1. `git init`
2. Creamos en la misma carpeta el archivo **.gitignore**.
    ```
    # Archivos de compilación de Python
    __pycache__/
    *.pyc

    # Archivos de pipenv. Sólo dejamos requirements.txt
    Pipfile
    Pipfile.lock

    # Deberíamos agregar la base de datos con:
    # db.sqlite3
    ```
3. `git add .`
4. `git commit -m "Primer commit"`
5. `git remote add origin https://github.com/<mi_cuenta_github>/<nombre_repositorio>.git`
6. `git branch -M main`
7. `git push -u origin main`
8. `git checkout -b clase_17-Django_Portfolio_Parte_1`
---

### Django
1. `django-admin startproject Clases_Coder`
2. `cd Clases_Coder`
3. `python manage.py migrate`
---
### Contenido de la clase
1. Primero creamos la función de Python que se encargará de devolver el código html al front. Para ello, debemos ingresar a la carpeta de configuración del proyecto y agregar un nuevo archivo llamado **views.py**.
2. En **views.py** agregamos una función:
    ```python
    from django.http import HttpResponse

    def saludo(request):
        return HttpResponse("Hola mundo!, hola Coder!")
    ```
3. En **urls.py**:
    ```python
    from django.contrib import admin
    from django.urls import path
    from .views import saludo

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludo/', saludo),
    ]
    ```
4. `python manage.py runserver`, y luego `localhost:8000/saludo/`
5. Ahora seguiremos los mismos pasos, pero vamos a enviar información desde el front hacia nuestro back mediante el método GET.
    Vamos a agregar la función dentro de **views.py**:
    ```python
    def muestra_nombre(request, nombre):
        return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")
    ```
6. En el archivo **urls.py**:
    ```python
    from django.contrib import admin
    from django.urls import path
    from .views import saludo, muestra_nombre

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludo/', saludo),
        path('muestra_nombre/<nombre>/', muestra_nombre),
    ]
    ```
7. Ya podemos probarlo modificando la url del navegador: `localhost:8000//muestra_nombre/Coder`
8. Usando plantillas:<br>
    Vamos a crear en la misma carpeta que venimos trabajando, una nueva carpeta con el nombre que deseen, para el ejemplo se llamará **plantillas**.
9. Dentro vamos a crear un archivo html, para el ejemplo se llamará **index.html**.
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
        Hola, esta es nuestra primer plantilla!
    </body>
    </html>
    ```
10. Generamos una nueva vista:
    ```python
    # Agregamos al encabezado del archivo el import de Template y de Context
    from django.template import Template, Context

    def probando_template(request):

        # Abrimos el archivo html
        mi_html = open('./Clases_Coder/plantillas/index.html')

        # Creamos el template haciendo uso de la clase Template
        plantilla = Template(mi_html.read())

        # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
        mi_html.close()

        # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
        mi_contexto = Context()

        # Terminamos de construír el template renderizándolo con su contexto
        documento = plantilla.render(mi_contexto)

        return HttpResponse(documento)
    ```
11. Editamos nuestro archivo **urls.py**:
    ```python
    from django.contrib import admin
    from django.urls import path
    from .views import saludo, muestra_nombre, probando_template

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludo/', saludo),
        path('muestra_nombre/<nombre>/', muestra_nombre),
        path('probando_template/', probando_template),
    ]
    ```
12. Ya podemos probar en nuestro navegador ingresando: `http://localhost:8000/probando_template/`
13. Desde la consola, vamos a detener el servidor presionando: `Ctrl + c`
---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git status`
    * Si estamos conformes, podemos enviarlos todos al **staging area** o ir agregando de a uno para evitar que se suba lo que no se desea subir. En caso de que hayan archivos que no queremos subir pero queremos que permanezcan siempre en el repositorio local, podemos agregarlos al **.gitignore**<br>
    Si vamos a subir los archivos seleccionándolos: `git add <nombre_archivo_1> <nombre_archivo_2> <nombre_archivo_3>`<br>
    Si vamos a subir todos los cambios: `git add .`
    * Realizamos el commit: `git commit -m "Paso 1 del proyecto: 1er clase"`
    * Vamos a subir nuestra rama a Github:<br>
    `git push --set-upstream origin clase_17-Django_Portfolio_Parte_I`
2. En Github realizamos un **Pull Request** (de ahora en más PR) y hacemos el merge a **main**.
---
---
## PROBLEMAS
1. Cuando no nos toma el entorno virtual, hay una solución que sirve para varios problemas:
    * Cerrar y volver a abrir VsCode.
    * Crear un archivo de Python temporalmente, sólo es para que VsCode seleccione un lenguaje y una versión.
    * Una vez seleccionado el archivo, VsCode nos indicará en la barra inferior derecha, el lenguaje **Python** y la versión utilizada **3.11**. Debemos hacer clic en la versión y se nos depliega una lista de opciones, donde se encuentran todas las versiones de Python que tenemos instaladas y los entornos virtuales, ahí elegimos el que acabamos de crear, cuyo nombre comienza con el de la carpeta raíz y luego tiene un hash agregado al final.<br>
    Una vez seleccionado el entorno ya podremos borrar el archivo de Python que habíamos creado y volvemos a abrir una consola. Deberíamos poder ver el entorno activado en la consola.