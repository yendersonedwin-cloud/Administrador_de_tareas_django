from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas
from .forms import TareaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_tareas(request):
    tareas = Tareas.objects.filter(usuario=request.user)
    return render(request, 'dashboard.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user 
            tarea.save()
            return redirect('dashboard') # Redirige si tiene éxito
        else:
            # Si el formulario falla, imprime el error en la terminal para saber por qué
            print(form.errors) 
            
    # Este return es VITAL: si no es POST o el formulario falla, vuelve al dashboard
    return redirect('dashboard')
@login_required
def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, id=tarea_id, usuario=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
    return redirect('dashboard')

@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tareas, id=tarea_id, usuario=request.user)
    tarea.delete()
    return redirect('dashboard')