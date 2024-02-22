# CLASES DE DJANGO EN CODERHOUSE

## Clase 24 - Playground Avanzado Parte III | Clase 8 de Django
---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`
2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.
3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_24-Playground_Avanzado_Parte_III`

---
### Edición de usuario
Los usuarios no son más que registros en la tabla **User** de la base de datos, por lo tanto, podemos aplicar CRUD tal como lo haríamos con cualquier otra tabla de datos.<br>
A continuación vamos a crear un formulario para editar los datos de un usuario.<br>

1. **editar_usuario.html**<br>
    El template recibirá desde la vista el formulario.
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Login {% endblock title %}

    {% block main %}
        <form action="" method="POST" enctype="multipart/form-data">
            {% csrf_token %}

            <table>

                {{ mi_form.as_table }}
                <input type="submit" value="Actualizar">

            </table>


        </form>

    {% endblock main %}
    ```

2. **views.py**
    ```python
    # Vista de editar el perfil
    # Obligamos a loguearse para editar los datos del usuario activo
    @login_required
    def editar_perfil(request):

        # El usuario para poder editar su perfil primero debe estar logueado.
        # Al estar logueado, podremos encontrar dentro del request la instancia
        # del usuario -> request.user
        usuario = request.user

        if request.method == 'POST':

            miFormulario = UserEditForm(request.POST)

            if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                # Datos que se modificarán
                usuario.email = informacion['email']
                usuario.password1 = informacion['password1']
                usuario.password2 = informacion['password1']
                usuario.save()

                # Retornamos al inicio una vez guardado los datos
                return render(request, "AppCoder/index.html")

        else:
            # Cuando el método es GET, podemos mostrar el formulario
            # con datos pre-cargados porque los conocemos del mismo usuario
            datos = {
                'first_name': usuario.first_name,
                'email': usuario.email
            }
            miFormulario = UserEditForm(initial=datos)

        return render(
            request,
            "users/editar_usuario.html",
            {
                "mi_form": miFormulario,
                "usuario": usuario
            }
        )
    ```

3. **urls.py**<br>
    Agregamos el siguiente path a la lista de **urlpatterns**
    ```python
    path('editar_usuario/', views.editar_usuario, name='EditarUsuario')
    ```

4. **forms.py**<br>
    A. Creamos el formulario heredando el mismo formulario de Django que usamos para crear un usuario nuevo.
    ```python
    class UserEditForm(UserCreationForm):

        # Obligatorios
        email = forms.EmailField(label="Ingrese su email:")
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ['email', 'password1', 'password2']
            help_texts = {k:"" for k in fields}
    ```

    B. Agregamos en el formulario más datos de la tabla User
    ```python
    class UserEditForm(UserCreationForm):

        # Obligatorios
        email = forms.EmailField(label="Ingrese su email:")
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
        # No obligatorios
        last_name = forms.CharField()
        first_name = forms.CharField()

        class Meta:
            model = User
            fields = [
                'email',
                'password1',
                'password2',
                'last_name',
                'first_name'
            ]
            help_texts = {k:"" for k in fields}
    ```

---
### Avatar
El avatar representa la imagen elegida por el usuario para su perfil. Vamos a crear el entorno para que el usuario pueda subir su imagen y mostrarla en la navbar.<br>
Pero antes, vamos a preparar la **navbar** para el uso del avatar y para incorporar también la opción de editar perfil desde un desplegable en la misma.

**templates/AppCoder/base.html**<br>
El primer paso va a ser agregar un Dropdown (botón desplegable) con las opciones que deseamos del usuario. Al mismo lo vamos a colocar al final de la navbar para que se vea en el navegador a la derecha de la misma.<br>
Luego agregaremos un condicional, ya que si un usuario aún no está autenticado, las opciones serán: "Iniciar sesión" y "Crear cuenta". Si está autenticado las opciones serán "Editar cuenta" y "Cerrar sesión". Para saber si el usuario que está navegando por el sitio está logueado podemos hacer uso del método `request.user.is_authenticated` en el propio `base.html` que nos devolverá **True** o **False** según esté o no logueado.
> NOTA: En el html sólo mostraremos el código de la navbar
```html
<!-- Navigation-->
<nav class="navbar navbar-expand-lg navbar-dark navbar-custom fixed-top">
    <div class="container px-5">
        <a class="navbar-brand" href="#page-top">Coder</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item"><a class="nav-link text-white" href="{% url 'Inicio' %}">Inicio</a></li>
                <li class="nav-item"><a class="nav-link text-white" href="{% url 'EstudianteList' %}">Estudiantes</a></li>
                <li class="nav-item"><a class="nav-link text-white" href="{% url 'ProfesorList' %}">Profesores</a></li>
                <li class="nav-item"><a class="nav-link text-white" href="{% url 'CursoList' %}">Cursos</a></li>
                <li class="nav-item"><a class="nav-link text-white" href="{% url 'EntregableList' %}">Entregables</a></li>
                
                
                {# DROPDOWN PARA LA CUENTA DE USUARIO #}
                {% if request.user.is_authenticated %}
                    <div class="dropdown">
                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            {{ request.user.username }}
                        </button>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <li><a class="dropdown-item" href="{% url 'Edit' %}">Editar cuenta</a></li>
                            <li><a class="dropdown-item" href="{% url 'Logout' %}">Cerrar sesión</a></li>
                        </ul>
                    </div>

                {% else %}

                    <div class="dropdown">
                        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Cuenta
                        </button>
                        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <li><a class="dropdown-item" href="{% url 'Login' %}">Inciar Sesión</a></li>
                            <li><a class="dropdown-item" href="{% url 'Register' %}">Crear cuenta</a></li>
                        </ul>
                    </div>
                {% endif %}
            </ul>
        </div>
    </div>
</nav>
```

1. **models.py**<br>
    Comenzaremos agregando un modelo nuevo que permita la carga de imágenes para luego asociarlo con un usuario, entonces, cuando un usuario ingrese a su cuenta y éste tenga cargada una imágen la buscaremos y la mostraremos en el template.
    > NOTA: No es práctico agregar imágenes en ninguna base de datos, lo que hacemos es guardar las imágenes en una carpeta del sistema y en la base de datos guardamos el path para saber a dónde debemos buscarla.
    ```python
    class Avatar(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
        imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

        def __str__(self):
            return f"{settings.MEDIA_URL}{self.imagen}"
    ```
    > **IMPORTANTE:** En las placas de Coder se utiliza la relación 1 a muchos (**models.ForeignKey**), esto genera por ejemplo, que si un usuario sube 10 fotos a su perfil, se guardarán las 10 fotos en el disco pero siempre se utilizará una de ellas quedando 9 archivos "basura" en el disco.<br>
    Pero nosotros estamos usando la relación 1 a 1 (**models.OneToOneField**) porque nos garantiza un archivo para cada cuenta de usuario y a medida que vamos agregando nuevas imágenes se van a ir eliminando las anteriores, por lo tanto siempre habrá una única imágen.

2. Ahora crearemos la carpeta para guardar las imágenes que los usuarios vayan subiendo, por convención se llama "media" y se coloca en el raíz del proyecto.<br>
    También debemos saber que en un principio dicha carpeta está vacía y además debe subirse vacía al repositorio de **Github**, el que se utilizará luego en el ambiente de producción. Una carpeta vacía será ignorada por **GIT**, lo que generará que la carpeta no se suba al repositorio de **Github** y por tanto el código que tengamos en el repositorio contendrá errores porque nunca encontrará dicha carpeta. Para evitar este error por convención agregamos un archivo a la carpeta que suele llamarse **.keep**. No necesita tener ningún contenido, sólo genera que la carpeta no quede vacía y por tanto **GIT** no ignorará la carpeta "media" y la subirá al repositorio de **Github**.

3. **settings.py**<br>
    A continuación, le vamos a indicar a Django mediante dos variables la ubicación de las imágenes y la url que apuntará a dicha ubicación.<br>
    Agregar en el settings:
    ```python
    # Indicamos la URL para acceder a la carpeta de imágenes
    MEDIA_URL = '/media/'
    # Indicamos cuál va a ser el path para llegar a la carpeta 
    # media que creamos en el paso anterior
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

4. **Clases_Coder/urls.py**<br>
    Ahora definimos en el archivo **urls.py** del proyecto los estáticos y la ubicación de los archivos haciendo uso de las variables creadas en el **settings.py**. Para ello debemos importar tanto el archivo **settings** del proyecto como el método estático para tal fin.
    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpaterns = [
        ...
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

5. Ahora vamos a aplicar los cambios que se hicieron en el modelo.<br>
    Desde la consola tipeamos:
    * `python manage.py makemigrations`
    * `python manage.py migrate`

6. **users/admin.py**<br>
    Agregamos el modelo al admin de Django.
    ```python
    from django.contrib import admin
    from users.models import Avatar

    admin.site.register(Avatar)
    ```

7. **base.html**<br>
    Ahora pasaremos a mostrar en la web la imagen que el usuario haya subido como su avatar. Agregamos en la navbar lo siguiente:
    ```html
    {% if request.user.is_authenticated %}
        <img src="{{(Avatar.objects.filter(user=request.user.id))[0].imagen.url}}"/>
        <p> class="text-muted small mb-4 -b-lg-0"> Hola, {{user.username}}!!!.</p>
    {% endif %}
    ```
    **views.py**<br>
    Otra manera sería enviándolo desde cada vista con el contexto:
    ```python
    @login_required
    def inicio(request):
        avatares = Avatar.objects.get(user=request.user)
        return render(
            request,
            "AppCoder/index.html",
            {"url": avatares.imagen.url}
        )
    ```


---
### Unit test












---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos Herencia e iniciamos el Admin de Django"`
    * `git push --set-upstream origin clase_20-Playground_intermedio_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
