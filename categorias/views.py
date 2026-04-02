from django.shortcuts import render
from .models import Categorias

def lista_categorias(request):
    # Traemos todas tus categorías de la base de datos
    categorias = Categorias.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})