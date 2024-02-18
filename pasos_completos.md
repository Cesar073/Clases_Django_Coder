# CLASES DE DJANGO EN CODERHOUSE

## CLASE 7: Clase 23 - Playground Avanzado Parte II

**Resumen:**<br>
Se crean formularios para la autenticación de usuarios. Un apartado para el login, logout y el registro. Al mismo tiempo se restringe el acceso a ciertas páginas del sitio para los usuarios que no estén debidamente logueados.<br>
El proyecto contiene creadas 3 cuentas de usuario para las pruebas:<br>
Coder_cuenta_super -> Pass: c0d3r_h0u53<br>
Coder_cuenta_staff -> Pass: c0d3r_h0u53<br>
Coder_cuenta_comun -> Pass: c0d3r_h0u53<br>

---
### Entorno virtual
Interpretamos que el entorno virtual es activado en cada clase.

---
### Git
1. Nos vamos a mover a la rama main, actualizarla y crear una nueva rama para la nueva clase:
    `git checkout main`

2. Actualizamos con: `git pull`. Esto se descarga los cambios que hayan en la rama main. Recordemos que el PR realizado en la clase anterior agregó archivos y modificaciones en la rama main.

3. Creamos y nos movemos a la nueva rama: `git checkout -b clase_23-Playground_Avanzado_Parte_II`

---
### Preparación
Para trabajar con los usuarios en ocaciones es recomendable trabajarlos en una app diferente de la lógica de negocio del proyecto, por esto es que vamos a crear una app "users" para este caso.

1. Creamos la app: `python manage.py startapp users`

2. Ingresamos al archivo de settings y agregamos en la lista **INSTALLED_APPS** la app recién creada `'users'`:
    ```python
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'AppCoder',
            'users'
        ]
    ```

3. Creamos el archivo de **urls.py** para la app "users":
    ```python
    from django.urls import path

    urlpatterns = []
    ```

4. Indicamos en el archivo **urls.py** del proyecto que incluya el **urls.py** que creamos recientemente:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('AppCoder.urls')),
        path('users/', include('users.urls'))
    ]
    ```

---
### Login
Vamos a crear una vista para solicitar al usuario el "username" y "password" para autenticarse.
1. Creamos un template, en este caso vamos a heredar de `templates/AppCoder/base.html`:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Login {% endblock title %}

    {% block main %}

        {# Este div sólo está agregado para centrar el formulario en la página usando Bootstrap #}
        <div class="d-flex justify-content-center">

            {# Con este div colocamos el título y debajo el formulario usando Bootstrap #}
            <div class="d-flex flex-column">

                {# Mensaje personalizado en la vista de Login con estilos de Bootstrap #}
                <p class="fs-5 fw-bold">{{ msg_login }}</p>

                <form action="" method="POST">
                    {% csrf_token %}
                    
                    {{ form.as_p }}
                    <input type="submit" value="Iniciar sesión">

                </form>

            </div>
        </div>
    {% endblock main %}
    ```

2. Actualizamos el archivo **urls.py** de la app de "users". Para ello vamos a importar el nuevo archivo **views.py** de ésta app y luego a agregar el path a la lista **urlpatterns**:
    ```python
    from django.urls import path
    from users import views

    urlpatterns = [
        path('login/', views.login_request, name="Login")
    ]
    ```

3. Vamos a crear la vista en el archivo **views.py**.
    ```python
    from django.shortcuts import render
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import login

    def login_request(request):

        msg_login = ""
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():

                usuario = form.cleaned_data.get('username')
                contrasenia = form.cleaned_data.get('password')

                user = authenticate(username=usuario, password=contrasenia)

                if user is not None:
                    login(request, user)
                    return render(request, "AppCoder/index.html")

            msg_login = "Usuario o contraseña incorrectos"

        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form, "msg_login": msg_login})
    ```

---
### Registro
A continuación, vamos a crear un formulario para que los usuarios puedan crearse una cuenta en nuestra plataforma. Dentro de las placas de Coder este apartado se realiza de 2 formas similares, vamos a detallarlas pero sólo vamos a aplicar la segunda opción.<br>
En la primer opción se crea en la vista (archivo **views.py**) un formulario importado de Django (**UserCreationForm**) para poder brindarle al usuario los campos necesarios para registrarse.<br>
Si bien esa opción es correcta, no se visualiza de manera agradable en el front, por lo tanto, en la segunda opción se decide modificar este apartado. Se crea el archivo **forms.py** y se crea un formulario personalizado que hereda de esta misma clase. Esta será la opción a incorporar. 
1. Comenzaremos por la vista en el archivo **views.py**. Como vamos a crear un formulario personalizado, primero vamos a importarlo y lo llamaremos **UserRegisterForm**. Luego aplicamos la lógica conocida para renderizar los formularios según el tipo de petición (GET o POST).<br>
    **views.py**
    ```python
    from .forms import UserRegisterForm

    def register(request):
    
        msg_register = ""
        if request.method == 'POST':

            form = UserRegisterForm(request.POST)
            if form.is_valid():
                # Si los datos ingresados en el form son válidos, con form.save()
                # creamos un nuevo user usando esos datos
                form.save()
                return render(request,"AppCoder/index.html")
            
            msg_register = "Error en los datos ingresados"

        form = UserRegisterForm()     
        return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})
    ```

2. Agregamos el path a las urls de la app "users": `path('register/', views.register, name="Register")`

3. Creamos el template `users/registro.html`:
    ```html
    {% extends 'AppCoder/base.html' %}

    {% load static %}

    {% block title %} Login {% endblock title %}

    {% block main %}

        {# Este div sólo está agregado para centrar el formulario en la página usando Bootstrap #}
        <div class="d-flex justify-content-center">

            {# Con este div colocamos el título y debajo el formulario usando Bootstrap #}
            <div class="d-flex flex-column">

                {# Mensaje personalizado en la vista de Login con estilos de Bootstrap #}
                <p class="fs-5 fw-bold">{{ msg_register }}</p>

                <form action="" method="POST">
                    {% csrf_token %}
                    
                    {{ form.as_p }}
                    <input type="submit" value="Registrarse">

                </form>

            </div>
        </div>
    {% endblock main %}
    ```

4. Creamos el formulario para el registro, para lo cuál vamos a requerir crear también el archivo **forms.py**. Este archivo va a requerir importar el formulario **UserCreationForm**.
    ```python
    from django import forms
    from django.contrib.auth.forms import UserCreationForm

    class UserRegisterForm(UserCreationForm):
        email = forms.EmailField()
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ["username", "email", "password1", "password2"]
            # Si queremos EDIAR los mensajes de ayuda editamos este dict,
                # de lo contrario lo limpiamos de ésta forma.
            help_text = {k: "" for k in fields}
    ```

---
### Logout
A continuación vamos a permitir que el usuario pueda cerrar sesión haciendo clic en un botón. A diferencia de los casos anteriores, el Logout no requiere una lógica adicional que deba agregar en sus vistas o un template específico, sólo debemos realizar un llamado a una vista de autenticación que importamos desde Django.
1. Importamos dicha vista y luego agregamos un path para el Logout.<br>
    **urls.py**:
    ```python
    from django.urls import path
    from users import views
    from django.contrib.auth.views import LogoutView

    urlpatterns = [
        path('login/', views.login_request, name="Login"),
        path('register/', views.register, name="Register"),
        path('logout/', LogoutView.as_view(template_name='AppCoder/index.html'), name="Logout")
    ]
    ```
    > NOTA: El parámetro **template_name** que le enviamos al método `LogoutView.as_view()`, indica el template al que se nos redirigirá una vez deslogueado.

2. Se puede crear una vista específica para mostrar una vez que el usuario se desloguea. Para el ejemplo que estámos realizando y a diferencia de las placas de Coder, no vamos a crear dicha vista sino que redirigimos al usuario al inicio (`index.html`).

---
### Mixin y Decoradores
Ahora requerimos restringir el acceso a las vistas que interactúan con la base de datos, para evitar que usuarios no logueados puedan modificar los registros de nuestras tablas. Para ello trabajaremos directamente con las vistas (**views.py**) y podemos implementar decoradores para las funciones o mixins para las vistas basadas en clases.

---
### Mixin - LoginRequiredMixin
Mixin es el nombre que adquieren las clases que se utilizan para extender la funcionalidad de otra clase mediante la herencia, por lo tanto, para limitar el acceso a usuarios que no se loguearon a una vista basada en clases lo único que requerimos es agregar y ubicar en el primer parámetros de herencias al **LoginRequiredMixin**. Tener en cuenta que ahora trabajaremos sobre el archivo de vistas que tenemos en la app "AppCoder" y no sobre "users".
**views.py** (sólo mostramos el código que se agrega y no el código completo del archivo)
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "AppCoder/curso_list.html"


class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "AppCoder/curso_detail.html"
```

---
### Decorador - login_required
Al igual que los mixins, los decoradores agregan funcionalidades pero en este caso a las funciones o métodos y ahora utilizaremos el decorador que permite hacer lo suyo en nuestras vistas basadas en funciones.
**views.py**
```python
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    return render(request, "AppCoder/about.html")
```

### Retoque final
Por último, debemos indicarle a Django cuál es nuestra página de logueo en los casos en que el usuario aún no se haya autenticado. De esta forma, si un usuario no se ha logueado pero intenta ingresar a una página que hemos limitado su acceso, éste debe ser redirigido a nuestra vista de login. Para ello debemos ingresar al **settings.py** del proyecto y agregar la siguiente línea: `LOGIN_URL = "/users/login/"`

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos login, registro y logout"`
    * `git push --set-upstream origin clase_23-Playground_Avanzado_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
