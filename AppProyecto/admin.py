from django.contrib import admin
from .models import Cliente,Ventas,Productos

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'mail')
    ordering = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Ventas)
class VentasAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'fecha', 'precio')
    ordering = ('nombre_cliente',)
    search_fields = ('nombre_cliente',)
    list_editable = ('precio',)

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('item', 'cantidad', 'precio')
    ordering = ('item',)
    search_fields = ('item',)
    list_editable = ('cantidad',)