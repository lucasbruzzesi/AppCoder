from django.urls import path
from .views import *
from AppPerfiles.views import *
from AppRegistro.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', inicio, name = 'InicioApp'),

    path('clientes/', listaclientes, name = 'Cliente'),
    path("editarcliente/<id>", editarclientes, name="editarcliente"),
    path("eliminarcliente/<id>", eliminarcliente, name="eliminarcliente"),
    path("agregar_nuevo_cliente", clientes, name="agregarnuevocliente"),

    path('productos/', listaproductos, name = 'Productos'),
    path("editarproducto/<id>", editarproductos, name="editarproducto"),
    path("eliminarproducto/<id>", eliminarproducto, name="eliminarproducto"),
    path("agregar_nuevo_producto", productos, name="agregarnuevoproducto"),

    path('ventas/', listaventas, name = 'Ventas'),
    path("editarventa/<id>", editarventas, name="editarventa"),
    path("eliminarventa/<id>", eliminarventa, name="eliminarventa"),
    path("agregar_nueva_venta", ventas, name="agregarnuevaventa"),

    path('buscar/', buscar, name="Buscar"),
    path('about/', about, name ='About'),
    
    path("accounts/login/", registrologin, name="login"),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path("accounts/signup/", registro, name="registro"),
    path("accounts/profile/", perfilusuario, name="perfilusuario"),
    path('accounts/editprofile/', editarPerfil, name='editarPerfil'),
    path('accounts/add_avatar/', agregarAvatar, name='agregarAvatar')
]