from django import forms

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="")