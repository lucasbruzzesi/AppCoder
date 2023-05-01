from django.shortcuts import render
from .models import Avatar
from .forms import AvatarForm

from django.contrib.auth.decorators import login_required

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = Avatar(user = request.user, imagen = request.FILES['imagen'])
            avatar_anterior = Avatar.objects.filter(user = request.user)
            if len(avatar_anterior)>0:
                avatar_anterior[0].delete()
            avatar.save()
            return render(request, 'AppProyecto/home.html', {'mensaje' : f'Tu avatar ha sido agregado', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/agregar_avatar.html', {'form' : form, 'usuario' : request.user, 'mensaje' : 'Error agregando el avatar'})
    else:
        form=AvatarForm()
        return render(request, 'AppProyecto/agregar_avatar.html', {'form' : form, 'usuario' : request.user, 'avatar' : obtener_avatar(request)})

def obtener_avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return '/media/avatares/defaultavatar.png'
