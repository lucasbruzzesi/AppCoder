from django import forms
from django.forms.widgets import NumberInput


METODOPAGO = [('Credito', ' Credito'), ('Debito', ' Debito'), ('Transferencia Bancaria', ' Transferencia Bancaria'), ('Mercado Pago', ' Mercado Pago')]


class ClienteForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre'}), max_length=20, label="")
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido'}), max_length=20, label="")
    pais = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Pais'}), max_length=20, label="")
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Ciudad'}), max_length=50, label="")
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Direccion'}), max_length=80, label="")
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label="")
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Telefono'}), max_length=20, label="")
    metodo_de_pago = forms.ChoiceField(widget=forms.RadioSelect, choices=METODOPAGO, label="Seleccionar forma de pago")
    
class ProductosForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Item'}), max_length=50, label="")
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Ingresar Descripcion del Producto'}), label="")
    cantidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Cantidad'}), max_length=50, label="")
    precio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Precio'}), max_length=50, label="")
    fecha_ingreso = forms.DateField(widget=NumberInput(attrs={'type':'date', 'class':'form-control'}), label="Seleccionar Fecha")

class ImagenProductoForm(forms.Form):
    imagen = forms.ImageField(label='')

class DetalleProductoForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Titulo'}), max_length=50, label="")
    imagen = forms.ImageField(label='')
    autor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Autor'}), max_length=50, label="")
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Ingresar Descripcion del Producto'}), label="")
    fecha = forms.DateField(widget=NumberInput(attrs={'type':'date', 'class':'form-control'}), label="Seleccionar Fecha")

class VentasForm(forms.Form):
    nombre_cliente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre del Cliente'}), max_length=50, label="")
    fecha = forms.DateField(widget=NumberInput(attrs={'type':'date', 'class':'form-control'}), label="Seleccionar Fecha")
    productos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Productos'}), max_length=50, label="")
    precio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Precio'}), max_length=20, label="")

class ReseñasForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Titulo'}), max_length=50, label="")
    autor = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Autor'}), max_length=50, label="")
    comentario = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Escribir Reseña'}), label="")
    valoracion = forms.ChoiceField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])