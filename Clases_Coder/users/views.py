from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserEditForm
from .forms import UserRegisterForm


# Create your views here.
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppCoder/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppCoder/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})

# Vista de registro
def register(request):

    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        # form = UserCreationForm()       
        form = UserRegisterForm()     

    return render(request,"users/registro.html" ,  {"form":form})

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/index.html")

    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "users/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
