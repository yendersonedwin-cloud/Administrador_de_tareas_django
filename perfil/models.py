from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    
    # Información Personal
    bio = models.TextField(max_length=500, blank=True, verbose_name="Biografía")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    
    # Redes Sociales (
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    github = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    
    
    foto = models.ImageField(upload_to='perfiles/', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return f'Perfil de {self.usuario.username}'