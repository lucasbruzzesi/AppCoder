from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    foto_perfil = models.ImageField(null=True, blank=True, upload_to='foto_perfil')

    def __str__(self):
        return f"{self.user}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"