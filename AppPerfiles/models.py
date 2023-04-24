from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    #para usar imagenes voy a tener que installar Pillow. de que manera?  pip install Pillow
