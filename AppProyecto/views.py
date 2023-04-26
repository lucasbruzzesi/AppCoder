from django.shortcuts import render
from .models import *
from .forms import *
from AppPerfiles.views import obtener_avatar

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



def inicio(request):
    return render(request, 'AppProyecto/inicio.html', {'avatar' : obtener_avatar(request)})



""" Funciones Clientes """

@login_required
def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.pais = form.cleaned_data['pais']
            cliente.ciudad = form.cleaned_data['ciudad']
            cliente.direccion = form.cleaned_data['direccion']
            cliente.mail = form.cleaned_data['mail']
            cliente.telefono = form.cleaned_data['telefono']
            cliente.metodopago = form.cleaned_data['metodo_de_pago']
            cliente.save()
            form = ClienteForm()
    else:
        form = ClienteForm()

    return render(request, 'AppProyecto/agregar_nuevo_cliente.html', {'form' : form, 'avatar' : obtener_avatar(request)})

@login_required
def editarclientes(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            cliente.nombre = info['nombre']
            cliente.apellido = info['apellido']
            cliente.pais = info['pais']
            cliente.ciudad = info['ciudad']
            cliente.direccion = info['direccion']
            cliente.mail = info['mail']
            cliente.telefono = info['telefono']
            cliente.metodopago = info['metodo_de_pago']
            cliente.save()
            clientes = Cliente.objects.all()
            form = ClienteForm()
            return render(request, 'AppProyecto/clientes.html', {'cliente': clientes, 'Mensaje': 'El cliente ha sido editado', 'form': form, 'avatar' : obtener_avatar(request)})
        pass
    else:
        formulario = ClienteForm(initial=
            {'nombre':cliente.nombre, 
            'apellido': cliente.apellido, 
            'pais': cliente.pais, 
            'ciudad': cliente.ciudad, 
            'direccion': cliente.direccion, 
            'mail': cliente.mail,
            'telefono': cliente.telefono,
            'metodo_de_pago': cliente.metodopago})
        return render(request, 'AppProyecto/editarcliente.html', {'cliente': cliente, 'form': formulario, 'avatar' : obtener_avatar(request)})

@login_required
def eliminarcliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    clientes = Cliente.objects.all()
    form = ClienteForm()
    return render(request, 'AppProyecto/clientes.html', {'cliente': clientes, 'form': form, 'avatar' : obtener_avatar(request)})

@login_required
def listaclientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'AppProyecto/clientes.html', {'cliente': clientes, 'avatar' : obtener_avatar(request)})



""" Funciones Ventas """

@login_required
def ventas(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            venta = Ventas()
            venta.nombre_cliente = form.cleaned_data['nombre_cliente']
            venta.fecha = form.cleaned_data['fecha']
            venta.productos = form.cleaned_data['productos']
            venta.precio = form.cleaned_data['precio']
            venta.save()
            form = VentasForm()
    else:
        form = VentasForm()

    return render(request, 'AppProyecto/agregar_nueva_venta.html', {"form": form, 'avatar' : obtener_avatar(request)})

@login_required
def editarventas(request, id):
    venta = Ventas.objects.get(id=id)
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            venta.nombre_cliente = info['nombre_cliente']
            venta.fecha = info['fecha']
            venta.productos = info['productos']
            venta.precio = info['precio']
            venta.save()
            ventas = Ventas.objects.all()
            form = VentasForm()
            return render(request, 'AppProyecto/ventas.html', {'ventas': ventas, 'Mensaje': 'La venta ha sido editada', 'form': form, 'avatar' : obtener_avatar(request)})
        pass
    else:
        formulario = VentasForm(initial=
            {'nombre_cliente':venta.nombre_cliente, 
            'fecha': venta.fecha, 
            'productos': venta.productos, 
            'precio': venta.precio})
        return render(request, 'AppProyecto/editarventa.html', {'venta': venta, 'form': formulario, 'avatar' : obtener_avatar(request)})

@login_required
def eliminarventa(request, id):
    venta = Ventas.objects.get(id=id)
    venta.delete()
    ventas = Ventas.objects.all()
    form = VentasForm()
    return render(request, 'AppProyecto/ventas.html', {'venta': ventas, 'form': form, 'avatar' : obtener_avatar(request)})

@login_required
def listaventas(request):
    ventas = Ventas.objects.all()
    return render(request, 'AppProyecto/ventas.html', {'ventas': ventas, 'avatar' : obtener_avatar(request)})



""" Funciones Productos """

@login_required
def productos(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            productos = Productos()
            productos.item = form.cleaned_data['item']
            productos.descripcion = form.cleaned_data['descripcion']
            productos.precio = form.cleaned_data['precio']
            productos.cantidad = form.cleaned_data['cantidad']
            productos.save()
            form = ProductosForm()
    else:
        form = ProductosForm()

    return render(request, 'AppProyecto/agregar_nuevo_producto.html', {"form" : form, 'avatar' : obtener_avatar(request)})

@login_required
def editarproductos(request, id):
    productos = Productos.objects.get(id=id)
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            productos.item = info['item']
            productos.descripcion = info['descripcion']
            productos.precio = info['precio']
            productos.cantidad = info['cantidad']
            productos.save()
            productos = Productos.objects.all()
            form = ProductosForm()
            return render(request, 'AppProyecto/productos.html', {'productos': productos, 'Mensaje': 'El producto ha sido editado', 'form': form, 'avatar' : obtener_avatar(request)})
        pass
    else:
        formulario = ProductosForm(initial=
            {'item':productos.item, 
            'descripcion': productos.descripcion, 
            'precio': productos.precio, 
            'cantidad': productos.cantidad,})
        return render(request, 'AppProyecto/editarproducto.html', {'producto': productos, 'form': formulario, 'avatar' : obtener_avatar(request)})

@login_required
def eliminarproducto(request, id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    productos = Productos.objects.all()
    form = ClienteForm()
    return render(request, 'AppProyecto/productos.html', {'productos': productos, 'mensaje': 'El producto ha sido borrado', 'form': form, 'avatar' : obtener_avatar(request)})

@login_required
def listaproductos(request):
    productos = Productos.objects.all()
    return render(request, 'AppProyecto/productos.html', {'productos': productos, 'avatar' : obtener_avatar(request)})



""" Funciones Busqueda """

@login_required
def buscar(request):
    
    nombre = request.GET["cliente"]
    form = ClienteForm(request.GET)
    if nombre!="":
        clientes = Cliente.objects.filter(nombre__contains=nombre)
        return render(request, "AppProyecto/resultadobusqueda.html", {"clientes": clientes, "form" : form, 'avatar' : obtener_avatar(request)})
    elif nombre == '':
        return render(request, "AppProyecto/resultadobusqueda.html", {"mensaje": 'Porfavor ingrese el nombre de un cliente', 'avatar' : obtener_avatar(request)})



""" Funciones 'Acerca de mi' """

def about(request):
    return render(request, 'AppProyecto/about.html', {'avatar' : obtener_avatar(request)})



""" Funcion para mostrar todos los datos de las listas """

@login_required
def listacompleta(request):
    productos = Productos.objects.all()
    ventas = Ventas.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'AppProyecto/pages.html', {'productos' : productos, 'ventas' : ventas, 'clientes' : clientes, 'avatar' : obtener_avatar(request)})