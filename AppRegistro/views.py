from django.shortcuts import render
from .forms import RegistroUsuarioForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

""" Funcion Login """

def registrologin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            infologin = form.cleaned_data

            usuario = infologin['nombre_usuario']
            clave = infologin['contraseña']
            usuariocheck = authenticate(nombre_usuario=usuario, contraseña=clave)

            if usuariocheck is not None:
                login(request, usuariocheck)
                return render(request, 'AppProyecto/inicio.html', {'mensaje': f'Usuario {usuario} ha iniciado sesion correctamente'})
            else:
                return render(request, 'AppProyecto/login.html', {'form': form, 'mensaje':'El usuario o la contraseña ingresados no son correctos'})
        else:
            return render(request, 'AppProyecto/login.html', {'form': form, 'mensaje':'El usuario o la contraseña ingresados no son correctos'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppProyecto/login.html', {'form':form})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            nombreusuario = form.cleaned_data.get('nombre_usuario')
            form.save()
            return render(request, 'AppProyecto/inicio.html', {'mensaje': f'Tu nuevo usuario {nombreusuario} se ha registrado con exito'})
        else:
            return render(request, 'AppProyecto/registro.html', {'form': form, 'mensaje':'Error creando usuario'})
    else:
        form = RegistroUsuarioForm()
        return render(request, 'AppProyecto/registro.html', {'form': form})
