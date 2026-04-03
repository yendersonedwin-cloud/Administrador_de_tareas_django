from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Esta función se activa SOLA cuando se guarda un Usuario
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        # Si el usuario es nuevo, le creamos su perfil
        Profile.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    # Esto asegura que si el usuario cambia algo, el perfil se guarde
    instance.perfil.save()