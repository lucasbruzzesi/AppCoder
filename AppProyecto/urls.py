from django.urls import path
from .views import *

urlpatterns = [

    path('', inicio, name = 'InicioApp'),
    path('clientes/', clientes, name = 'Cliente'),
    path('ventas/', ventas, name = 'Ventas'),
    path('productos/', productos, name = 'Productos'),
    path("buscar/", buscar, name="buscar"),
]