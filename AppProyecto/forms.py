from django import forms
from django.forms.widgets import NumberInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


TIPOTARJETA = [('Visa', ' Visa'), ('Mastercard', ' Mastercard'), ('Otros', ' Otros')]

class ClienteForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre'}), max_length=20, label="")
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido'}), max_length=20, label="")
    pais = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Pais'}), max_length=20, label="")
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Ciudad'}), max_length=50, label="")
    direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Direccion'}), max_length=80, label="")
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label="")
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Telefono'}), max_length=20, label="")
    tipo_tarjeta = forms.ChoiceField(widget=forms.RadioSelect, choices=TIPOTARJETA, label="Seleccionar tipo de tarjeta")
    
class ProductosForm(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Item'}), max_length=50)
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Ingresar Descripcion del Producto'}))
    cantidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Cantidad'}), max_length=50)
    precio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Precio'}), max_length=50)

class VentasForm(forms.Form):
    nombre_cliente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre del Cliente'}), max_length=50)
    fecha = forms.DateField(widget=NumberInput(attrs={'type':'date', 'class':'form-control'}))
    productos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Productos'}), max_length=50)
    precio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Precio'}), max_length=20)