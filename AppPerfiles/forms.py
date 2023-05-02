from django import forms
from .models import Conversacion,Mensaje

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="")

class ConversacionForm(forms.ModelForm):
    class Meta:
        model = Conversacion
        fields = ['participantes']

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['remitente', 'contenido', 'destinatario', 'conversacion']