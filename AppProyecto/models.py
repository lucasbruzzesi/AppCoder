from django.db import models

# Create your models here.
class Cliente(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    mail = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipotarjeta = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido}' 

class Ventas(models.Model):

    nombre_cliente = models.CharField(max_length=50)
    fecha = models.CharField(max_length=10)
    productos = models.CharField(max_length=50)
    precio = models.CharField(max_length=20)

class Productos(models.Model):

    item = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    cantidad = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)