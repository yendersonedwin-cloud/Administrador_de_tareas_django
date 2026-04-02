from django.db import models
from colorfield.fields import ColorField

class Categorias(models.Model):
    PRIORIDAD_CHOICES = [
        ('A', 'Alta'),
        ('M', 'Media'),
        ('B', 'Baja'),
    ]

    nombre = models.CharField(max_length=100)
    color = ColorField(default='#3498db')
    prioridad = models.CharField(max_length=1, choices=PRIORIDAD_CHOICES, default='M')

    # Función mágica para el color automático de la prioridad
    def get_prioridad_color(self):
        if self.prioridad == 'A':
            return "#FF0000" # Rojo
        elif self.prioridad == 'M':
            return "#FFC107" # Amarillo
        else:
            return "#28A745" # Verde

    def __str__(self):
        return f"{self.nombre} ({self.get_prioridad_display()})"

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"