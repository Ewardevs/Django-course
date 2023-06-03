from django.urls import path
from . import views

urlpatterns = [
    path("",views.agregar_contacto,name="agregar_contacto"),
    path("eliminar_contacto/<int:id>/",views.eliminar_contacto,name="eliminar_contacto")
]


