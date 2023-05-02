from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField(null = True)

    def __str__(self):
        return f'{self.user}'


class Avatar(models.Model):
    imagen = models.ImageField(upload_to = 'avatares')
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.imagen}'


class Conversacion(models.Model):
    participantes = models.ManyToManyField(User, related_name='Conversaciones')
    fecha_creacion_conversacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ','.join([str(participante) for participante in self.participantes.all()])


class Mensaje(models.Model):
    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, related_name='Mensajes')
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    contenido = models.TextField()
    fecha_mensaje = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensaje de {self.remitente} to {self.destinatario}: {self.contenido}'