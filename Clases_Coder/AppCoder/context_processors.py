# context_processors.py
from django.contrib.auth.context_processors import auth
from users.models import Imagen

def custom_user(request):
    context = auth(request)
    user = context['user']

    if user.is_authenticated:
        imagen = Imagen.objects.filter(user=request.user.id)
        cant = len(imagen)
        if cant > 0:
            context['user_avatar'] = imagen[cant-1]
        else:
            context['user_avatar'] = ""

    return context
