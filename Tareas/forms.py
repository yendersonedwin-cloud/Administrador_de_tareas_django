from django import forms
from .models import Tareas
#El forms es el puente entre la BD y el usuario     
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'estado', 'fecha_limite', 'categoria']
    
    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        # Hacemos que estos campos no sean obligatorios para que el 
        # formulario de creación rápida del dashboard funcione.
        self.fields['descripcion'].required = False
        self.fields['estado'].required = False
        self.fields['fecha_limite'].required = False
        self.fields['categoria'].required = False
        # fields son llos camplos que el usuario va ver y a editar
        

        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Estudiar para el parcial'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
