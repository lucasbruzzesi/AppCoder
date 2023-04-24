from django.shortcuts import render
from .models import Avatar
from .forms import AvatarForm

from django.contrib.auth.decorators import login_required

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES['imagen'])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppProyecto/inicio.html", {'mensaje' : f'Avatar agregado correctamente', 'avatar' : obtenerAvatar(request)})
        else:
            return render(request, "AppProyecto/agregar_avatar.html", {'form' : form, 'usuario' : request.user, 'mensaje' : "Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppProyecto/agregar_avatar.html", {'form' : form, 'usuario' : request.user, 'avatar' : obtenerAvatar(request)})

def obtenerAvatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
        return avatares[0].imagen.url
    else:
        return "/media/avatares/avatarpordefecto.png"

@login_required
def editarPerfil(request):
    pass

@login_required
def perfilusuario(request):
    pass
