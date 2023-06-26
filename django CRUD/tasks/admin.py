from django.contrib import admin

# Register your models here.
from .models import *

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

admin.site.register(Task,TaskAdmin)