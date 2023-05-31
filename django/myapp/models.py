from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=200)
    
    # esto da el nombre del pryecto eb la pantalla de administrados
    
    def __str__(self):
        return self.name

# esto crear una tabla importante en la referencia llamar models.Model para poder crear
# CharField es para caracteres
# TextField para textos peqeños

class task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    # ForeignKEy es para relaxionar con otras tablas,dentro de () colocar con que tabla se relaciona
    # y luego el on_delete para que la app sepa que hacer si se elimina un projecto,
    # en este caso cuando se eliina un projecto todas las tablas que estan relacionada principalmente
    # se eliminaran  siguente de la tabla, todo esto para por que se usa el models.CASCADE que hace 
    # que se elimine lo relacionado
    
    project = models.ForeignKey(project,on_delete=models.CASCADE)
    
    done = models.BooleanField(default=False)
    
    
    # esto da en la pantalla de administrador el titludo de la tarea y de que projecto va
    def __str__(self):
        return self.title + " - " + self.project.name
    
    
# mi modeló
class alumnos(models.Model):
    nombre_alumno = models.CharField(max_length=200)
    edad_alumno = models.IntegerField()
    
    proyecto = models.ForeignKey(project,on_delete=models.CASCADE)
    
