# CLASES DE DJANGO EN CODERHOUSE

## CLASE 4: Clase 21 - Playground intermedio Parte III
---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`
2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.
3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_21-Playground_intermedio_Parte_III`

---
### Formularios
¿Cómo funcionan los formularios?<br>
El html recibe nuestra información por medio de la vista y su template asociado. Al apretar un botón  esa información viaja por medio de un método GET o POST y llega al servidor, donde esos datos se manipulan.<br>
El método GET se utiliza para hacer consultas o búsquedas a nuestro servicio.<br>
El método POST para los momentos en los que se envía información. Ya sea para crear, modificar o eliminar información almacenada en nuestro proyecto.<br><br>

**Creación de formularios (HTML)**
1. Creamos una vista nueva en **views.py**:
    ```python
    from django.shortcuts import render

    def curso_formulario(request):
        return render(request, "AppCoder/curso_formulario.html")
    ```
2. Agregamos el path en **urls.py**:
    ```python
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario")
    ```
3. Creamos el archivo HTML donde vamos a agregar el formulario:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Formulario - Agregar Curso {% endblock title %}

    {% block main %}
        <!-- action: representa la url a la que nos va a re-dirigir y enviar la info.
        Tiene prioridad por sobre la redirección que podamos colocar en views.py -->
        <form action="/CursoFormulario/" method="POST">
            {% csrf_token %}
            <p>Curso: <input type="text" name="curso"></p>
            <p>Camada: <input type="text" name="camada"></p>

            <input type="submit" value="Enviar">

        </form>
    {% endblock main %}
    ```
4. Editamos la vista (**views.py**) para trabajar con los datos recibidos en el POST:
    ```python
    from django.shortcuts import render

    def curso_formulario(request):

        if request.method == 'POST':

            curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
            curso.save()

            return render(request, "AppCoder/index.html")

        return render(request,"AppCoder/curso_formulario.html")
    ```

---
### Creación de formularios (API from Django)
Django nos provee una API para crear formularios de una manera más simple, dominar esta API nos facilitará la creación de los mismos incluyendo validación de campos entre otros beneficios.
1. En la app Clases_Coder creamos un nuevo archivo **forms.py**.<br>
    Similar a la creación de modelos para la base de datos, vamos a crear cada campo de nuestro form pero heredando de `from django import forms`:
    ```python
    from django import forms

    class CursoFormulario(forms.Form):
        curso = forms.CharField()
        camada = forms.IntegerField()
    ```
2. Adecuamos la vista (**views.py**) para recibir generar y recibir el formulario recién creado:
    ```python
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
3. Creamos un html (**form_con_api.html**) preparado para recibir el formulario de Django:
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
Vamos a utilizar el mismo tipo de formulario pero en este caso serán para realizar búsquedas. En las placas hay una versión para el uso de formularios creados con HTML, pero vamos a usar la API de Django ya que es lo que se va a solicitar para la pre-entrega.<br>
1. Agregar path en el archivo **urls.py** para la vista donde realizamos la búsqueda:
    ```python
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
    ```
2. Creamos la función en **views.py** para llamar al template con su formulario:
    ```python
    def buscar_form_con_api(request):
        if request.method == "POST":
            miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                
                cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

                return render(request, "AppCoder/resultados_buscar_form.html", {"cursos": cursos})
        else:
            miFormulario = BuscaCursoForm()

        return render(request, "AppCoder/buscar_form_con_api.html", {"miFormulario": miFormulario})
    ```

3. Creamos el template (**buscar_form_con_api.html**) con un form:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Buscar Curso {% endblock title %}

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
4. Creamos el template **mostrar_cursos.html** que hacemos referencia en la vista (**views.py**) cuando tenemos resultados para mostrar:
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

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos Herencia e iniciamos el Admin de Django"`
    * `git push --set-upstream origin clase_20-Playground_intermedio_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
