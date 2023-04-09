from django.urls import path
from .views import *

urlpatterns = [

    path('', inicioapp, name = 'InicioApp'),
    path('Cliente/', Cliente1, name = 'Cliente'),
    path('Carrito/', carrito, name = 'Carrito'),
    path('Productos', productos, name = 'Productos'),

]