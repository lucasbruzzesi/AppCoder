from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre de Usuario'}), max_length=20, label='')
    mail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar Contraseña'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}), label='')

    class Meta:
        model = User
        fields = ["username", "mail", "password1", "password2"]

class UserEditForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre'}), max_length=20, label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido'}), max_length=20, label='')
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Ingresar Una Biografia'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingresar Mail'}), label='')
    link = forms.URLField(widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'Ingresar Link Laboral o Social'}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar Contraseña'}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}), label='')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio', 'email', 'link', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre de Usuario'}), max_length=20, label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresar Contraseña'}), label='')