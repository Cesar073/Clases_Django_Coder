from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='AppCoder/index.html'), name="Logout"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('cambiar_pass/', views.CambiarPasswordView.as_view(), name="CambiarPass"),
]
