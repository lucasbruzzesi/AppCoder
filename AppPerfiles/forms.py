from django import forms
from .models import Perfil

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('bio', 'foto_perfil')

		
		widgets = {
			'bio': forms.Textarea(attrs={'class': 'form-control'}),
			'foto_perfil': forms.TextInput(attrs={'class': 'form-control'}),
			'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'link' : forms.TextInput(attrs={'class': 'form-control'})		
		}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")