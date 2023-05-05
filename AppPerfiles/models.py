from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):

    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField(null = True)

    class Meta: 
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f'{self.user}'


class Avatar(models.Model):
    imagen = models.ImageField(upload_to = 'avatares')
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta: 
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"

    def __str__(self):
        return f'{self.user} - {self.imagen}'




# class Conversacion(models.Model):
#    participantes = models.ManyToManyField(User)
#    fecha_creacion_conversacion = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return ','.join([str(participante) for participante in self.participantes.all()])


# class Mensaje(models.Model):
#    conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, related_name='Mensajes')
#    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
#    contenido = models.TextField()
#    fecha_mensaje = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f'Mensaje de {self.remitente} to {self.destinatario}: {self.contenido}'