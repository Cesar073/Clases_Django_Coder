from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Clase 24
class Imagen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"