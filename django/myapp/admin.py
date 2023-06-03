from django.contrib import admin

# Aca importamos nuestros modelos
from .models import *


# con esto hacemos que en el panel de administrador se vea la id 
class projectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class alumnosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_alumno']
    list_display_links = ['id', 'nombre_alumno']


# Register your models here.
# esto es para poner tus modelos(tablas) en la pagina de admin de Django
admin.site.register(project, projectAdmin)
admin.site.register(task)
admin.site.register(alumnos,alumnosAdmin)