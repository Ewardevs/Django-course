from django.db import models
import datetime

# Create your models here.
class Categorias(models.Model):
    categoria = models.CharField(max_length=200)
    
    def __str__(self):
        return  self.categoria
    
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=200)
    publicacion = models.TextField(max_length=2000)
    fecha_subida = models.DateField(default=datetime.date.today)
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE)
    
    def __str__(self):
        return  self.titulo + " - "+ str(self.categoria)
    
    