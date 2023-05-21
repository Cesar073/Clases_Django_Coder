# CLASES DE DJANGO EN CODERHOUSE

## CLASE 1: Clase 17 - Django - Portfolio Parte I
---

### Entorno virtual.
1. Creamos la carpeta donde trabajaremos en nuestro proyecto de Django.
2. Abrimos VsCode posicionándonos en dicha carpeta.
3. Si no tenemos instalado el gestor de entornos virtuales **pipenv**, abrimos la termina desde VsCode `ctrl + j` y lo instalamos:<br>
    `pip install pipenv`
4. Si queremos seleccionar una versión de Python específica para nuestro proyecto debemos tenerla instalada en la PC. Luego podemos crear el entorno con el siguiente comando:<br>
    `pipenv --python 3.9.13`
5. Usamos un mismo comando para crear o activar el entorno virtual:<br>
    `pipenv shell`<br>
    El entorno virtual queda indicado en la consola con un prefijo similar a esto:<br>`(nombre_entorno_virtual) C:\path_donde_estamos_ubicados`<br>
    De no ser así, hay varias formas de solucionarlo, ver: **(1) Problemas**
---

### Instalaciones
1. Creamos el archivo de **requirements.txt**, el cuál por el momento sólo va a tener la versión de Django que deseemos. También es buena práctica indicar a modo de comentario la versión de Python que usamos para el proyecto.
    ```
    # Python 3.9.13
    django==4.2
    ```
2. lo ejecutamos con pipenv:<br>
    `pipenv install -r requirements.txt`
---

### GitHub
* En este apartado no explicaremos demasiado, sólo vamos a crear el repositorio y obtenemos la url para vincularlo con el repositorio local de Git.
---

### Git
**NOTA IMPORTANTE:** Todos los comandos que se hagan sobre Git, deben ejecutarse con la consola ubicada en la posición donde se encuentra la carpeta **.git** y no dentro del proyecto de Django, esto suele ser un error ya que los comandos que ejecutemos de Git va a tener dificultades con algunos comandos si generamos cambios en carpetas que no puede ver.
1. Creamos el repositorio ejecutando en la consola: `git init`
2. Creamos en la misma carpeta el archivo **.gitignore**.
    NOTA: Debería agregarse la base de datos para evitar que se suba como parte del repositorio, pero para el curso vamos a subirla para quién requiera descargar el repositorio ya cuente con datos agregados.
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
3. Pasamos al **staging area** los archivos **.gitignore** y **requirements.txt**:<br>
    `git add .`
4. Hacemos el primer commit:<br>
    `git commit -m "Primer commit"`
5. Linkeamos nuestro repositorio de Git con el que hemos creado en Github:
    `git remote add origin https://github.com/<mi_cuenta_github>/<nombre_repositorio>.git`
6. Si en local tenemos la rama **master**, vamos a cambiarle el nombre por **main**:
    `git branch -M main`
7. Subimos los cambios que hicimos en local al repositorio de Github:
    `git push -u origin main`
8. Creamos una nueva rama a partir de ésta instancia del **main** y nos movemos a la nueva rama, en nuestro ejemplo se va a llamar **clase_17-Django_Portfolio_Parte_1**:<br>
    `git checkout -b clase_17-Django_Portfolio_Parte_1`
---

### Django
1. Creamos un proyecto de Django. Con el siguiente comando vamos a crear una carpeta en la posición en que nos encontramos y luego dentro de la misma se cargarán los archivos del proyecto:<br>
    `django-admin startproject <nombre_del_proyecto>`<br>
    Ej: `django-admin startproject Clases_Coder`
2. Debido a que hemos creado una subcarpeta, debemos ingresar a la misma para poder interactuar con el archivo **manage.py** de Django:<br>
    `cd <nombre_del_proyecto>`<br>
    Ej: `cd Clases_Coder`
3. Corremos las migraciones. Si bien no es obligatorio, éstas migraciones de Django van a crear las tablas necesarias para el Admin de Django, cuentas de usuario, etc. Asimismo con esta acción evitamos los mensajes de advertencia al iniciar el servidor:<br>
    `python manage.py migrate`
4. Opcional: Ya estamos en condiciones de correr el servidor y comprobar que el proyecto está correctamente creado. Con el siguiente comando, Django crea un servidor y lo corre bajo el puerto 8000:<br>
    * `pyhton manage.py runserver`
    * Nos dirigimos al navegador y colocamos `localhost:8000` o bien mantemos presionado `Ctrl` y hacemos clic en el link que nos figura en la consola: `http://127.0.0.1:8000/`
---

### Contenido de la clase
**Resumen:** Vamos a crear nuestras primeras interacciones desde el front con nuestro back. Esto permitirá que modificando la url del navegador, se pueda dirigir a una página simple pero con el contenido que nosotros queremos compartir.<br>
1. Primero creamos la función de Python que se encargará de devolver el código html al front. Para ello, debemos ingresar a la carpeta de configuración del proyecto y agregar un nuevo archivo llamado **views.py**. La carpeta de configuración del proyecto se encuentra dentro de la carpeta del propio proyecto con su mismo nombre, podemos distinguirla porque dicha carpeta contiene los archivos: `__init__.py, asgi.py, settings.py, urls.py, wsgi.py`
2. En el archivo que acabamos de crear **views.py**, agregamos una función que será la encargada de crear el archivo html y devolvérselo al front. Para el ejemplo vamos a crear la función llamada **saludo** y sólo devolverá un texto al front. Debe contener:
    ```python
    from django.http import HttpResponse

    def saludo(request):
        return HttpResponse("Hola mundo!, hola Coder!")
    ```
3. En la misma carpeta, tenemos el archivo **urls.py**, vamos a editarlo para que la url apunte a la función que acabamos de crear. Por lo tanto, vamos a importar la función (`from .views import saludo`) y luego agregamos el **path** dentro de la lista de path's llamada **urlpatterns** para definir la url que se debrerá ingresar en el navegador y que la misma nos redirija a dicha función (`path('saludo/', saludo)`). El archivo debe quedar de la siguiente manera:
    ```python
    from django.contrib import admin
    from django.urls import path
    from .views import saludo

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('saludo/', saludo),
    ]
    ```
4. Podemos comprobar los resultados levantando el servidor ejecutando en la consola: `python manage.py runserver`, y luego agregando a la url dentro del navegador la nueva página: `localhost:8000/saludo/`
5. Enviando valores usando el método GET:<br>
    Ahora seguiremos los mismos pasos, pero vamos a enviar información desde el front hacia nuestro back mediante el método GET, el cuál se ejecuta cuando modificamos la url, por lo tanto, en la url vamos a incorporar una variable. En nuestro ejemplo vamos a enviar un nombre y el back creará una página con dicha información. Cabe aclarar que el back puede utilizar ese dato para realizar diversas tareas, como buscar en la base de datos, realizar peticiones a otros servicios, etc.<br>
    Vamos a agregar la función dentro de **views.py**, y dentro de sus parámetros vamos a recibir la variable llamada **nombre**:
    ```python
    def muestra_nombre(request, nombre):
        return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")
    ```
6. En el archivo **urls.py** importamos la función y creamos el path dentro de la lista **urlpatterns** para que nos redirija a la función recién creada y además le indicamos que pueda recibir un parámetro extra bajo el nombre de variable **nombre**:
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
7. Ya podemos probarlo modificando la url del navegador: `localhost:8000//muestra_nombre/Coder`<br>
    Debería aparecer la frase que creamos en la función del **views.py** con el nombre de "Coder", el cuál podemos modificarlo sin problemas desde la url del navegador.
8. Usando plantillas:<br>
    A continuación vamos a crear un archivo html y que sea dicho archivo el que se envíe al front.<br>
    Para esto, vamos a crear en la misma carpeta que venimos trabajando, una nueva carpeta con el nombre que deseen, para el ejemplo se llamará **plantillas**.
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
10. Generamos una nueva vista, o sea, una nueva función en el archivo **views.py** que en vez de retornar texto como lo hicimos anteriormente, vamos a retornar el archivo html. Como el código se empieza a extender, sólo mostramos los agregados al archivo y no el contenido completo:
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
11. Editamos nuestro archivo **urls.py** para crear una url que nos redirija a la función recién creada:
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
    * `git add .`
    * `git commit -m "Paso 1 del proyecto: 1er clase"`
    * `git push --set-upstream origin clase_17-Django_Portfolio_Parte_I`
2. En Github realizamos un **Pull Request** (de ahora en más PR) y hacemos el merge a **main**.
---
---

## PROBLEMAS
1. Cuando no nos toma el entorno virtual, hay una solución que sirve para varios problemas:
    * Cerrar y volver a abrir VsCode.
    * Crear un archivo de Python temporalmente, sólo es para que VsCode seleccione un lenguaje y una versión.
    * Una vez seleccionado el archivo, VsCode nos indicará en la barra inferior derecha, el lenguaje **Python** y la versión utilizada **3.11**. Debemos hacer clic en la versión y se nos depliega una lista de opciones, donde se encuentran todas las versiones de Python que tenemos instaladas y los entornos virtuales, ahí elegimos el que acabamos de crear, cuyo nombre comienza con el de la carpeta raíz y luego tiene un hash agregado al final.<br>
    Una vez seleccionado el entorno ya podremos borrar el archivo de Python que habíamos creado y volvemos a abrir una consola. Deberíamos poder ver el entorno activado en la consola.