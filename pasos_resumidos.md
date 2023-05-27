# CLASES DE DJANGO EN CODERHOUSE

## CLASE 3: Clase 19 - Playground intermedio Parte I
---
### Entorno virtual
De ahora en más, vamos a interpretar que el entorno virtual es activado en cada clase.

---
### Git
1. `git checkout main`
2. `git pull`
3. `git checkout -b clase_19-Playground_intermedio_Parte_I`

---
### Limpiamos vistas
**views.py:**
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

---
### Django: Urls avanzadas
**Para crear nuestras vistas en una app:**
1. Crear en la app **AppCoder** un archivo de **urls.py**:
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
2. Editamos el archivo **urls.py** que teníamos dentro de la carpeta principal:
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
from django.shortcuts import render
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
#### Agregamos los templates en una APP
1. Ingresar a la web: [Bootstrap - Templates](https://startbootstrap.com/templates), elegimos una plantilla general, la descargamos y descomprimimos.
2. Creamos: `static/AppCoder` y `templates/AppCoder`.
3. Colocamos los archivos donde correspondan.

Ahora hacemos referencia en **views.py**:
1. Indicamos en **AppCoder/views.py** apunte a nuestro nuevo index, o sea, el **index.html**:
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse

    def inicio(request):
        return render(request, "AppCoder/index.html")
    ```
2. `{% load static %}`
    ```html
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
