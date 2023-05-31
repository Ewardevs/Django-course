from django.urls import path
from . import views

urlpatterns = [
    path('categoria/',views.categoria),#
    path('publicacion/',views.publicacion),
    path('publicacion/<str:categoria>',views.publicacion_categoria),
    path('descripcion/<str:titulo>',views.descripcion) #
]


