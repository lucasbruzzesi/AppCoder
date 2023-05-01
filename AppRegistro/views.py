from django.shortcuts import render
from .forms import RegistroUsuarioForm, UserEditForm, LoginForm
from AppPerfiles.views import obtener_avatar
from AppPerfiles.models import Perfil
from django.contrib.auth import login, authenticate



""" Funcion Login """

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

def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.nombre = info['first_name']
            usuario.apellido = info['last_name']
            usuario.bio = info['bio']
            usuario.email = info['email']
            usuario.link = info['link']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.save()
            return render(request, 'AppProyecto/Principal.html', {'mensaje' : f'Usuario {usuario.username} editado correctamente', 'avatar' : obtener_avatar(request)})
        else:
            return render(request, 'AppProyecto/edit_profile.html', {'form' : form, 'nombreusuario' : usuario.username, 'avatar' : obtener_avatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, 'AppProyecto/edit_profile.html', {'form' : form, 'nombreusuario' : usuario.username, 'avatar' : obtener_avatar(request)})

def usuariocompleto(request):
    perfiles = Perfil.objects.all()
    return render(request, 'AppProyecto/profile.html', {'perfiles' : perfiles, 'avatar' : obtener_avatar(request)})
