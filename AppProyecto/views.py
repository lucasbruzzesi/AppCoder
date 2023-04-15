from django.shortcuts import render
from .models import Cliente,Ventas,Productos
from .forms import ClienteForm,VentasForm,ProductosForm

def inicio(request):
    return render(request, 'AppProyecto/inicio.html')

def clientes(request):
    if request.method == "POST":
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
            cliente.tipotarjeta = form.cleaned_data['tipo_tarjeta']
            cliente.save()
            form = ClienteForm()
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'AppProyecto/clientes.html', {"clientes": clientes, "form" : form})

def ventas(request):
    if request.method == "POST":
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

    venta = Ventas.objects.all()
    return render(request, 'AppProyecto/ventas.html', {"ventas": venta, "form" : form})

def productos(request):
    if request.method == "POST":
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

    productos = Productos.objects.all()
    return render(request, 'AppProyecto/productos.html', {"productos": productos, "form" : form})

def buscar(request):
    
    nombre= request.GET["cliente"]
    form = ClienteForm(request.GET)
    if nombre!="":
        clientes= Cliente.objects.filter(nombre__contains=nombre)
        return render(request, "AppProyecto/resultadobusqueda.html", {"clientes": clientes, "form" : form})