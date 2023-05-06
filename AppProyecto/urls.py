from django.urls import path
from .views import *
from AppPerfiles.views import *
from AppRegistro.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('', inicio, name = 'InicioApp'),

# URLS Formularios

    path('clientes/', listaclientes, name='Cliente'),
    path("editarcliente/<id>", editarclientes, name="editarcliente"),
    path("eliminarcliente/<id>", eliminarcliente, name="eliminarcliente"),
    path("agregar_nuevo_cliente", clientes, name="agregarnuevocliente"),

    path('productos/', listaproductos, name='Productos'),
    path("editarproducto/<id>", editarproductos, name="editarproducto"),
    path("eliminarproducto/<id>", eliminarproducto, name="eliminarproducto"),
    path("agregar_nuevo_producto", productos, name="agregarnuevoproducto"),

    path('ventas/', listaventas, name='Ventas'),
    path("editarventa/<id>", editarventas, name="editarventa"),
    path("eliminarventa/<id>", eliminarventa, name="eliminarventa"),
    path("agregar_nueva_venta", ventas, name="agregarnuevaventa"),

#URL Busquedas

    path('buscar/', buscar, name="Buscar"),
    path('buscar_productos/', buscar_productos, name="BuscarProducto"),
    path('buscar_ventas/', buscar_ventas, name="BuscarVenta"),

#URLS Inicio

    path('about/', about, name ='About'),
    path('pages/', listacompleta, name ='Pages'),

# URLS Profile

    path("login/", registro_login, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("signup/", registro, name="registro"),
    path('profile/<id>', usuariocompleto, name="perfilusuario"),
    path('edit_profile/<id>', editar_perfil, name='editarPerfil'),
    path('agregar_avatar/', agregar_avatar, name='agregarAvatar'),
    path("eliminaravatar", eliminaravatar, name="eliminaravatar")

#    path('messages/', ConversacionListView.as_view(), name='ListaConversaciones'),
#    path('add_conversation/', IniciarConversacionView.as_view(), name='AgregarConversacion'),
#    path('chat/', ChatListView.as_view(), name='Chat'),
#    path('write_message/', ChatView.as_view(), name='EscribirMensaje')
]