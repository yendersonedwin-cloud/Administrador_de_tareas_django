from django.urls import path
from . import views

urlpatterns = [
    
    path('lista/', views.lista_categorias, name='lista_categorias'),
]