from django import forms
from django.forms.widgets import NumberInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

class VentasForm(forms.Form):
    nombre_cliente = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre del Cliente'}), max_length=50, label="")
    fecha = forms.DateField(widget=NumberInput(attrs={'type':'date', 'class':'form-control'}), label="Seleccionar Fecha")
    productos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Productos'}), max_length=50, label="")
    precio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Precio'}), max_length=20, label="")

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre de Usuario'}), max_length=20, label="")
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar Contraseña'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}), label='')

    class Meta:
        model=User
        fields=["username", "mail", "password1", "password2"]
        help_texts = {k:"" for k in fields}