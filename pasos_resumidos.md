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
1. `git checkout main`
2. `git pull`
3. `git checkout -b clase_23-Playground_Avanzado_Parte_II`

---
### Preparación
1. Creamos la app: `python manage.py startapp users`
2. Actualizamos **INSTALLED_APPS**:
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
3. **users/urls.py**:
    ```python
    from django.urls import path

    urlpatterns = []
    ```
4. **Clases_Coder/urls.py**:
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
1. Creamos un template `templates/AppCoder/base.html`:
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

2. **users/urls.py**:
    ```python
    from django.urls import path
    from users import views

    urlpatterns = [
        path('login/', views.login_request, name="Login")
    ]
    ```

3. **views.py**:
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
1. **views.py**:
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

4. Creamos el formulario **users/forms.py**:
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
1. **urls.py**:
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

---
### Mixin - LoginRequiredMixin
**views.py**:
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
**views.py**:
```python
from django.contrib.auth.decorators import login_required

@login_required
def about(request):
    return render(request, "AppCoder/about.html")
```

### Retoque final
**settings.py**: `LOGIN_URL = "/users/login/"`

---
### Subimos los cambios a GitHub
1. Subimos los cambios a nuestro repositorio de GitHub:
    * `git add .`
    * `git commit -m "Agregamos login, registro y logout"`
    * `git push --set-upstream origin clase_23-Playground_Avanzado_Parte_II`
2. En Github realizamos un PR y hacemos el merge a **main**.
