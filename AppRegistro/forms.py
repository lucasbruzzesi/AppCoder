from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre de Usuario'}), max_length=20, label="")
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar Contraseña'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}), label='')

    class Meta:
        model=User
        fields=["username", "mail", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    nombre_del_usuario=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre'}), max_length=20, label="")
    apellido_del_usuario=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido'}), max_length=20, label="")
    mail= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label='')
    link=forms.URLField(widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'Ingresar Link Laboral o Social'}), label="")
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar Contraseña'}), label='')
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}), label='')

    class Meta:
        model=User
        fields=['email', 'nombre_del_usuario', 'apellido_del_usuario', 'mail', 'link', 'password1', 'password2']
        help_texts = {k:"" for k in fields}