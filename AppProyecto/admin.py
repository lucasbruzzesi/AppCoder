from django.contrib import admin
from .models import Cliente,Ventas,Productos

admin.site.register(Cliente)
admin.site.register(Ventas)
admin.site.register(Productos)