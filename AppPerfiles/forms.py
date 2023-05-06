from django import forms
# from .models import Conversacion,Mensaje

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label='')


class PerfilForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre'}), max_length=20, label="")
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Apellido'}), max_length=20, label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Email'}), max_length=50, label="")
    link = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Link'}), max_length=200, label="")





























#class ConversacionForm(forms.ModelForm):
#    class Meta:
#        model = Conversacion
#        fields = ['participantes']

#class MensajeForm(forms.ModelForm):
#    class Meta:
#        model = Mensaje
#        fields = ['remitente', 'contenido', 'destinatario', 'conversacion']