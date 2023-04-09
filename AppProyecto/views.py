from django.shortcuts import render
from .models import Cliente
from AgregarCliente import Cliente1
from django.http import HttpResponse

def agregar_clientes(request):

    Cliente1=Cliente()
    Cliente1.save()
    return HttpResponse()

def clientes(request):
    return render(request, 'AppProyecto/clientes.html')

def carrito(request):
    return render(request, 'AppProyecto/carrito.html')

def productos(request):
    return render(request, 'AppProyecto/productos.html')

def inicio(request):
    return HttpResponse('Bienvenido a la pagina de inicio')

def inicioapp(request):
    return render(request, 'AppProyecto/inicio.html')