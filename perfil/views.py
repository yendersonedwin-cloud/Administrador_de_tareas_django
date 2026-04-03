from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from .models import Profile
from Tareas.models import Tareas 

@login_required
def editar_perfil(request):
    # Obtenemos el perfil del usuario logueado
    perfil = get_object_or_404(Profile, usuario=request.user)
    
    if request.method == 'POST':
        # 1. Actualizamos datos del Usuario 
        request.user.first_name = request.POST.get('nombre')
        request.user.email = request.POST.get('email')
        request.user.save()
        
        # 2. Actualizamos datos del Perfil 
        perfil.bio = request.POST.get('bio')
        perfil.telefono = request.POST.get('telefono')
        perfil.instagram = request.POST.get('instagram')
        perfil.facebook = request.POST.get('facebook')
        
        # Manejo de la foto
        if 'foto' in request.FILES:
            perfil.foto = request.FILES['foto']
            
        
        perfil.save()
        
        
        messages.success(request, "¡Tu perfil se ha actualizado correctamente!")
        
        return redirect('profile') 

    
    mis_tareas = Tareas.objects.filter(usuario=request.user)
    total = mis_tareas.count()
    # Asegúrate de que 'Completada' sea el nombre exacto en tu modelo de Tareas
    completadas = mis_tareas.filter(estado='Completada').count() 
    porcentaje = int((completadas / total) * 100) if total > 0 else 0

    context = {
        'perfil': perfil,
        'total_tareas': total,
        'completadas': completadas,
        'porcentaje': porcentaje,
    }
    return render(request, 'profile.html', context)