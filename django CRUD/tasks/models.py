from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(blank=True,null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title +" - "+ self.user.username
    

class Amistad(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
    )
    usuario1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amistades_usuario1')
    usuario2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amistades_usuario2')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario1.username} - {self.usuario2.username}"
