# CLASES DE DJANGO EN CODERHOUSE

## CLASE 3: Clase 19 - Playground intermedio Parte I
---
### Entorno virtual
De ahora en más, vamos a interpretar que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`
2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.
3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_19-Playground_intermedio_Parte_I`

---
### Limpiamos vistas
Cuando creamos el proyecto anterior, hemos creado las vistas (**views.py**) y agregamos las urls asociadas a esas vistas. Lo que no estaba correcto es crear y modificar estos archivos en la carpeta principal de configuración del proyecto, por lo tanto, eliminamos de la carpeta Clases_Coder/Clases_Coder/views.py y luego restauramos el archivos de **urls.py**.
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
A partir de ahora vamos a crear las vistas dentro de las aplicaciones.<br>
Para el cambio aplicado podemos hacer un commit y luego continuar.

---
### Django: Urls avanzadas
Resumen:<br>
Por más que nuestro proyecto sea simple, rápidamente puede contenter múltiples páginas, tengamos en cuenta que una única tabla de nuestra base de datos muchas veces requiere hasta 4 páginas para poder realizar un CRUD en la misma. Si a eso sumamos index, about y más tablas, rápidamente contaremos con múltiples vistas por más que contemos con un proyecto relativamente pequeño.<br>
Para solucionar ésto podemos crear aplicaciones (de Django) donde no sólo contenemos nuestra base de datos, sino también podemos generar las vistas asociadas a dicha app. Asimismo, estructurar con aplicaciones nuestro proyecto nos facilita enormemente escalarlo o realizar cambios sobre el mismo en la medida en que lo necesitemos.<br>
**Para crear nuestras vistas en una app:**
>NOTA: Continuamos el proceso trabajando sobre el proyecto actual, donde contamos con nuestra AppCoder.
1. Crear en la app **AppCoder** un archivo de **urls.py** con los path a los cuáles queremos agregar al proyecto:
```python
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('/', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables)
]
```
2. En el archivo **urls.py** que teníamos dentro de la carpeta principal de configuración del proyecto, vamos a dejar el acceso al admin y en vez de cargar un path para cada una de nuestras vistas, vamos a incluír todo el archivo **urls.py** que acabamos de crear en la app, de la siguiente manera:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls'))
]
```

3. Creamos en el archivo de **views.py** (en la app se crea automáticamente) las vistas a realizar, por el momento serán sencillas:
```python
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Vista inicio")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")
```
>NOTA: Ya podemos probar su funcionamiento levantando el servidor.

---
### Agregamos los templates en una APP

Resumen:<br>
A partir de ahora vamos a perfeccionar nuestro front haciendo uso de plantillas creadas en Bootstrap o pueden ser extraídas de otra web.<br>
A continuación, un "paso a paso" para ver cómo incorporar una plantilla creada en bootstrap:<br>
1. Ingresar a la web: [Bootstrap - Templates](https://startbootstrap.com/templates)<br>
    Podemos buscar entre múltiples tipos de páginas, pero nosotros vamos a filtrar en las de propósito general y gratuitas.
2. Una vez en la web, seleccionamos la que más se ajuste a nuestro proyecto y hacemos clic.
3. Hacemos clic en **Free Donwnload**.
4. Una vez descargado el archivo `.zip`, podemos descomprimirlo y llevar sus carpetas a nuestro proyecto.
5. Para nuestro caso donde tenemos una app llamada **AppCoder**, vamos a ingresar a dicha carpeta y crear 2 nuevas carpetas: `static/AppCoder` y `templates/AppCoder`.
    Es decir, dentro de la carpeta de la app tenemos que crear **static** y **templates**, pero dentro de cada una de ellas vamos a crear una nueva carpeta con el mismo nombre de la app a la que pertenecen.
6. Dentro de `templates/AppCoder` vamos a colocar nuestros archivos `.html`.
7. Dentro de la carpeta `static/AppCoder` vamos a colocar las demás carpetas descargadas de Bootstrap, que suelen ser: `assets - css - js`.
    
Ahora lo que nos falta es indicarle a nuestras funciones en **views.py** que rendericen el html recién cargado junto a los archivos estáticos (assets, css y js):
1. Indicamos en **AppCoder/views.py** apunte a nuestro nuevo index, o sea, el **index.html**.
2. Vamos a editar el index para que Django luego sepa cargar los archivos estáticos del mismo:
    - Debemos colocar en el inicio del archivo (puede ser la primer línea dentro del <head>), la siguiente sintaxis: `{% load static %}`
    - Luego, modificamos los links o referencias a todos los archivos externos al html (css, js, img, etc), cambiando:
    ```html
    ESTO
    <link href="css/styles.css" rel="stylesheet" />
    
    POR ESTO
    <link href="{% static 'AppCoder/css/styles.css' %}" rel="stylesheet" />
    ```
3. Ya estamos en condiciones de editar el archivo html a mano para que concuerde con nuestro proyecto.

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Paso 3 del proyecto: 3er clase"`
    * `git push --set-upstream origin clase_19-Playground_intermedio_Parte_I`
2. En Github realizamos un PR y hacemos el merge a **main**.
