from users.models import Avatar
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import os

@receiver(pre_save, sender=Avatar)
def delete_avatar_file(sender, instance, **kwargs):
    # Eliminar el archivo de avatar cuando se borra el objeto Avatar
    if instance.imagen:
        old_path = Avatar.objects.get(user=instance.user.id).imagen.path
        if os.path.isfile(old_path):
            os.remove(old_path)
