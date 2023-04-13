from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    pais = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=80)
    mail = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    tipo_tarjeta = forms.CharField(max_length=20)
    
class ProductosForm(forms.Form):
    item = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=50)
    cantidad = forms.CharField(max_length=50)
    precio = forms.CharField(max_length=50)

class VentasForm(forms.Form):
    nombre_cliente = forms.CharField(max_length=50)
    fecha = forms.CharField(help_text='DD/MM/YY')
    productos = forms.CharField(max_length=50)
    precio = forms.CharField(max_length=20)