# CLASES DE DJANGO EN CODERHOUSE

## CLASE 4: Clase 21 - Playground intermedio Parte III
---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. `git checkout main`
2. `git pull`
3. `git checkout -b clase_21-Playground_intermedio_Parte_III`

---
### Formularios
**Creación de formularios (HTML)**
1. **views.py**:
    ```python
    from AppCoder.models import Curso

    def curso_formulario(request):

        if request.method == 'POST':

            curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
            curso.save()

            return render(request, "AppCoder/index.html")

        return render(request,"AppCoder/curso_formulario.html")
    ```
2. **urls.py**:
    ```python
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario")
    ```
3. **curso_formulario.html**:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Formulario - Agregar Curso {% endblock title %}

    {% block main %}
        <!-- action: representa la url a la que nos va a re-dirigir y enviar la info.
        Tiene prioridad por sobre la redirección que podamos colocar en views.py -->
        <form action="/curso-formulario/" method="POST">
            {% csrf_token %}
            <p>Curso: <input type="text" name="curso"></p>
            <p>Camada: <input type="text" name="camada"></p>

            <input type="submit" value="Enviar">

        </form>
    {% endblock main %}
    ```

---
### Creación de formularios (API from Django)
1. **urls.py**:
    ```python
    from django.urls import path
    from AppCoder import views

    urlpatterns = [
        path('', views.inicio, name="Inicio"),
        path('profesores/', views.profesores, name="Profesores"),
        path('estudiantes/', views.estudiantes, name="Estudiantes"),
        path('cursos/', views.cursos, name="Cursos"),
        path('entregables/', views.entregables, name="Entregables"),
        path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
        path('form-con-api/', views.form_con_api, name="FormConApi")
    ]
    ```
2. **forms.py**:
    ```python
    from django import forms

    class CursoFormulario(forms.Form):
        curso = forms.CharField()
        camada = forms.IntegerField()
    ```
3. **views.py**:
    ```python
    from AppCoder.forms import CursoFormulario

    def form_con_api(request):
        if request.method == "POST":
            mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            # print(miFormulario)
            if mi_formulario.is_valid():
                informacion = mi_formulario.cleaned_data
                
                curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                curso.save()

                return render(request, "AppCoder/index.html")
        else:
            mi_formulario = CursoFormulario()

        return render(request, "AppCoder/form_con_api.html", {"mi_formulario": mi_formulario})
    ```
4. **form_con_api.html**:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Formulario con API {% endblock title %}

    {% block main %}
        <!-- En este ejemplo dejamos el action vacío ya que lo manejamos desde la vista -->
        <form action="" method="POST">
            {% csrf_token %}
            
            <table>
                {{ mi_formulario.as_table }}
            </table>
            <input type="submit" value="Enviar">

        </form>
    {% endblock main %}
    ```

---
### Búsqueda con Form
1. **urls.py**:
    ```python
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
    ```
2. **views.py**:
    ```python
    from AppCoder.forms import BuscaCursoForm

    def buscar_form_con_api(request):
        if request.method == "POST":
            mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

            if mi_formulario.is_valid():
                informacion = mi_formulario.cleaned_data
                
                cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

                return render(request, "AppCoder/mostrar_cursos.html", {"cursos": cursos})
        else:
            mi_formulario = BuscaCursoForm()

        return render(request, "AppCoder/buscar_form_con_api.html", {"mi_formulario": mi_formulario})
    ```

3. **buscar_form_con_api.html**:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Buscar Curso {% endblock title %}

    {% block main %}
        <form action="" method="POST">
            {% csrf_token %}
            <table>
                {{ mi_formulario.as_table }}
            </table>
            <input type="submit" value="Enviar">

        </form>
    {% endblock main %}
    ```
4. **mostrar_cursos.html**:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Inicio {% endblock title %}

    {% block main %}


    {% for curso in cursos %}
        <li>Curso: {{ curso.nombre }} | Camada: {{ curso.camada }}</li>
    {% endfor %}


    {% endblock main %}

    ```
5. **forms.py**:
    ```python
    class BuscaCursoForm(forms.Form):
        curso = forms.CharField()
    ```

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos formularios para guardar y buscar cursos"`
    * `git push --set-upstream origin clase_21-Playground_intermedio_Parte_III`
2. En Github realizamos un PR y hacemos el merge a **main**.
