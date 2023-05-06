from .forms import RegistroUsuarioForm, UserEditForm, LoginForm
from AppPerfiles.views import obtener_avatar

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



# Funciones Login

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'AppProyecto/home.html', {'mensaje': f'Tu nuevo usuario {username} se ha registrado con exito', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/signup.html', {'form': form, 'mensaje':'Error creando usuario', 'avatar' : obtener_avatar(request)})
    else:
        form = RegistroUsuarioForm()
        return render(request, 'AppProyecto/signup.html', {'form': form, 'avatar' : obtener_avatar(request)})

def registro_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)

        if form.is_valid():
            infologin = form.cleaned_data

            usuario = infologin['username']
            clave = infologin['password']
            usuariocheck = authenticate(username=usuario, password=clave)
            form.error_messages = {}

            if usuariocheck is not None:
                login(request, usuariocheck)
                return render(request, 'AppProyecto/home.html', {'mensaje': f'Usuario {usuario} ha iniciado sesion correctamente', 'avatar' : obtener_avatar(request)})
            else:
                return render(request, 'AppProyecto/login.html', {'form': form, 'mensaje':'Los datos ingresados no son correctos', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/login.html', {'form': form, 'mensaje':'Los datos ingresados no son correctos', 'avatar' : obtener_avatar(request)})
    else:
        form = LoginForm()
        return render(request, 'AppProyecto/login.html', {'form':form, 'avatar' : obtener_avatar(request)})

# Funciones Perfil

def editar_perfil(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.email = info['email']
            usuario.link = info['link']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            return render(request, 'AppProyecto/profile.html', {'avatar' : obtener_avatar(request)})
        else:
            form=UserEditForm(instance=usuario)
            return render(request, 'AppProyecto/edit_profile.html', {'form' : form, 'nombreusuario' : usuario.username, 'usuario': usuario, 'avatar' : obtener_avatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, 'AppProyecto/edit_profile.html', {'form' : form, 'nombreusuario' : usuario.username, 'avatar' : obtener_avatar(request)})

def usuariocompleto(request, id):
    usuario = User.objects.get(id=id)
    return render(request, 'AppProyecto/profile.html', {'usuario' : usuario, 'avatar' : obtener_avatar(request)})
