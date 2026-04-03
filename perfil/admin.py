from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('usuario', 'telefono', 'instagram', 'facebook') 
    
    # Esto añade un buscador por nombre de usuario o teléfono
    search_fields = ('usuario__username', 'telefono')
