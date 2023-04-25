from django.shortcuts import render
from .forms import RegistroUsuarioForm, UserEditForm
from AppPerfiles.views import obtener_avatar

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

""" Funcion Login """

def registro_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            infologin = form.cleaned_data

            usuario = infologin['username']
            clave = infologin['password']
            usuariocheck = authenticate(username=usuario, password=clave)

            if usuariocheck is not None:
                login(request, usuariocheck)
                return render(request, 'AppProyecto/inicio.html', {'mensaje': f'Usuario {usuario} ha iniciado sesion correctamente', 'avatar' : obtener_avatar(request)})
            else:
                return render(request, 'AppProyecto/login.html', {'form': form, 'mensaje':'El usuario o la contraseña ingresados no son correctos', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/login.html', {'form': form, 'mensaje':'El usuario o la contraseña ingresados no son correctos', 'avatar' : obtener_avatar(request)})
    else:
        form = AuthenticationForm()
        return render(request, 'AppProyecto/login.html', {'form':form, 'avatar' : obtener_avatar(request)})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppProyecto/inicio.html', {'mensaje': f'Tu nuevo usuario {username} se ha registrado con exito', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/registro.html', {'form': form, 'mensaje':'Error creando usuario', 'avatar' : obtener_avatar(request)})
    else:
        form = RegistroUsuarioForm()
        return render(request, 'AppProyecto/registro.html', {'form': form, 'avatar' : obtener_avatar(request)})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.mail=info['mail']
            usuario.password1=info['password1']
            usuario.password2=info['password2']
            usuario.nombre=info['nombre']
            usuario.apellido=info['apellido']
            usuario.save()
            return render(request, 'AppProyecto/principal.html', {'mensaje' : f'Usuario {usuario.username} editado correctamente', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/editarperfil.html', {'form' : form, 'nombreusuario' : usuario.username, 'avatar' : obtener_avatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, 'AppProyecto/editarperfil.html', {'form' : form, 'nombreusuario' : usuario.username, 'avatar' : obtener_avatar(request)})
