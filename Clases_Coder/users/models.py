from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Clase 24
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    @property
    def d(self):
        return self.user.last_name

    def __str__(self):
        return f"{self.user} - {self.imagen}"
