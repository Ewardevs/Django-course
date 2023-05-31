from django.contrib import admin

from .models import project,task,alumnos


# con esto hacemos que en el panel de administrador se vea ñla id 
class projectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

# Register your models here.
 # esto es para poner tus modelos en la pagina de admin
admin.site.register(project,projectAdmin)
admin.site.register(task)
admin.site.register(alumnos)

